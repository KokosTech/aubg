"""Provides the main train simulation service logic."""

import json

from errors.custom_exceptions import NotFoundError
from models.journey import Journey
from models.rail.rail_network import RailNetwork
from models.trains.base import BaseTrain
from models.trains.helper.carriage import Carriage, CarriageType
from models.trains.helper.stop import Stop
from models.trains.intercity import IntercityTrain
from models.trains.intercity_express import IntercityExpressTrain
from models.trains.passenger import PassengerTrain
from services.validate_train_schedule import validate_train_schedule
from utils.config import MIN_TRANSFER_TIME
from utils.time import Time


class TrainSim:
    def __init__(self, rail_network: RailNetwork):
        self._rail_network = rail_network
        self._trains: dict[str, BaseTrain] = {}

    @property
    def trains(self):
        return self._trains

    @property
    def rail_network(self):
        return self._rail_network

    # ============
    # == Trains ==
    # ============

    def add_train(self, train: BaseTrain):
        if not isinstance(train, BaseTrain):
            raise TypeError("train must be a BaseTrain instance")
        if train.train_id in self._trains:
            raise ValueError(f"Train '{train.train_id}' already exists")

        self._trains[train.train_id] = train

    def remove_train(self, train_id: str):
        if train_id not in self._trains:
            raise ValueError(f"Train '{train_id}' not found")

        self._trains.pop(train_id)

    def get_train(self, train_id: str) -> BaseTrain:
        if train_id not in self._trains:
            raise ValueError(f"Train '{train_id}' not found")

        return self._trains[train_id]

    def add_stop_to_train(self, train_id: str, stop: Stop, duration_minutes: int = 1):
        train = self.get_train(train_id)
        train.append_stop(stop, duration_minutes)

        # used to check if the schedule is possible - according to track speed
        try:
            validate_train_schedule(train, self._rail_network)
        except ValueError as e:
            train.stops.remove(stop)
            print(f"Error adding stop: {e}")
            raise

    # ===========================================
    # ==     Train Helpers for Rail Network    ==
    # == used for deleting tracks and stations ==
    # ===========================================

    def get_trains_using_station(self, station_name: str) -> list[str]:
        train_ids = []

        for train_id, train in self._trains.items():
            if any(stop.station.name == station_name for stop in train.stops):
                train_ids.append(train_id)

        return train_ids

    def get_trains_using_track(self, from_station: str, to_station: str) -> list[str]:
        train_ids = []

        for train_id, train in self._trains.items():
            # Check if train has consecutive stops using this track
            for i in range(len(train.stops) - 1):
                current_station = train.stops[i].station.name
                next_station = train.stops[i + 1].station.name
                if current_station == from_station and next_station == to_station:
                    train_ids.append(train_id)
                    break

        return train_ids

    def remove_trains_using_station(self, station_name: str) -> list[str]:
        removed_ids = self.get_trains_using_station(station_name)
        for train_id in removed_ids:
            self.remove_train(train_id)

        return removed_ids

    def remove_trains_using_track(self, from_station: str, to_station: str) -> list[str]:
        removed_ids = self.get_trains_using_track(from_station, to_station)
        for train_id in removed_ids:
            self.remove_train(train_id)

        return removed_ids

    # ============
    # == Search ==
    # ============

    def search_journeys(
            self,
            from_station: str,
            to_station: str,
            departure_time: Time | None = None,
            direct_only: bool = False,
            sort_by: str = "departure_time"
    ) -> list[Journey]:
        if from_station not in self._rail_network.stations:
            raise ValueError(f"Station '{from_station}' not found")
        if to_station not in self._rail_network.stations:
            raise ValueError(f"Station '{to_station}' not found")
        if from_station == to_station:
            raise ValueError("from_station and to_station must be different")

        direct = self._find_direct(from_station, to_station, departure_time)

        if direct_only:
            return self._sort_journeys(direct, sort_by)

        one_transfer = self._find_with_transfers(
            from_station, to_station, departure_time, max_transfers=1
        )
        two_transfers = self._find_with_transfers(
            from_station, to_station, departure_time, max_transfers=2
        )

        return (
                self._sort_journeys(direct, sort_by) +
                self._sort_journeys(one_transfer, sort_by) +
                self._sort_journeys(two_transfers, sort_by)
        )

    # =======================
    # == Search Algorithms ==
    # =======================

    def _find_direct(
            self,
            from_station: str,
            to_station: str,
            departure_time: Time | None
    ) -> list[Journey]:
        results = []
        for train in self._trains.values():
            if not self._comes_before(train, from_station, to_station):
                continue

            board = self._get_stop(train, from_station)
            alight = self._get_stop(train, to_station)

            if board is None or alight is None:
                continue
            if board.departure_time is None or alight.arrival_time is None:
                continue
            if departure_time and board.departure_time < departure_time:
                continue

            results.append(Journey(
                legs=[train],
                boarding_stops=[board],
                alighting_stops=[alight]
            ))
        return results

    def _find_with_transfers(
            self,
            from_station: str,
            to_station: str,
            departure_time: Time | None,
            max_transfers: int
    ) -> list[Journey]:
        results = []
        visited = {from_station}

        # the actual algorithm - it's pretty stupid
        # the algorithm is a limited dfs (limited by max_transfers) that tries to find ANY path from from_station to to_station
        # in a perfect world with proper time management, I would've implemented it using A* or Djikstra's
        # TODO: implement a better algorithm in the summer
        def search(current_station, dept_time, legs, boardings, alightings, transfers_left):
            if transfers_left == 0:
                return

            for via in self._rail_network.stations:
                if via in visited or via == to_station:
                    continue

                visited.add(via)
                intermediates = self._find_direct(
                    current_station, via, dept_time)

                for leg in intermediates:
                    arrival = leg.alighting_stops[0].arrival_time
                    next_dept = arrival + MIN_TRANSFER_TIME

                    # try to reach destination from via
                    final_legs = self._find_direct(via, to_station, next_dept)
                    for final in final_legs:
                        results.append(Journey(
                            legs=legs + [leg.legs[0], final.legs[0]],
                            boarding_stops=boardings + [leg.boarding_stops[0], final.boarding_stops[0]],
                            alighting_stops=alightings + [leg.alighting_stops[0], final.alighting_stops[0]]
                        ))

                    # recurse deeper if transfers remain
                    search(
                        via,
                        next_dept,
                        legs + [leg.legs[0]],
                        boardings + [leg.boarding_stops[0]],
                        alightings + [leg.alighting_stops[0]],
                        transfers_left - 1
                    )

                visited.discard(via)

        search(from_station, departure_time, [], [], [], max_transfers)
        return results

    # ====================
    # == Search Helpers ==
    # ====================

    def _get_stop(self, train: BaseTrain, station_name: str) -> Stop | None:
        matches = [s for s in train.stops if s.station.name == station_name]
        return matches[0] if matches else None

    def _comes_before(self, train: BaseTrain, from_station: str, to_station: str) -> bool:
        names = [s.station.name for s in train.stops]
        if from_station not in names or to_station not in names:
            return False
        return names.index(from_station) < names.index(to_station)

    def _sort_journeys(self, journeys: list[Journey], sort_by: str) -> list[Journey]:
        if sort_by == "duration":
            return sorted(journeys, key=lambda j: j.total_duration)
        return sorted(journeys, key=lambda j: j.departure_time)

    # =====================
    # == File I/O Trains ==
    # =====================

    def save_trains_to_json(self, filename: str):
        data = []
        for train in self._trains.values():
            data.append({
                "type": type(train).__name__,
                "train_id": train.train_id,
                "name": train.name,
                "carriages": [
                    {
                        "carriage_type": c.carriage_type.value,
                        "capacity": c.capacity
                    }
                    for c in train.carriages
                ],
                "stops": [
                    {
                        "station": s.station.name,
                        "arrival_time": [s.arrival_time.hour, s.arrival_time.minute] if s.arrival_time else None,
                        "departure_time": [s.departure_time.hour, s.departure_time.minute] if s.departure_time else None
                    }
                    for s in train.stops
                ]
            })
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving to {filename}: {e}")

    def load_trains_from_json(self, filename: str):
        self._trains.clear()
        data = dict()

        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, IOError) as e:
            print(f"Continuing with empty train set. Error loading from {filename}: {e}")
            raise

        if not isinstance(data, list):
            raise ValueError("Invalid trains JSON format: root should be a list")

        train_classes = {
            "PassengerTrain": PassengerTrain,
            "IntercityTrain": IntercityTrain,
            "IntercityExpressTrain": IntercityExpressTrain
        }

        for item in data:
            try:
                train_class = train_classes.get(item["type"])
                if train_class is None:
                    raise ValueError(f"Unknown train type: {item['type']}")

                carriages = [
                    Carriage(CarriageType(
                        c["carriage_type"].lower()), c["capacity"])
                    for c in item["carriages"]
                ]

                stops = [
                    Stop(
                        station=self._rail_network.get_station(s["station"]),
                        arrival_time=Time(
                            s["arrival_time"][0], s["arrival_time"][1]
                        ) if s["arrival_time"] else None,
                        departure_time=Time(
                            s["departure_time"][0], s["departure_time"][1]
                        ) if s["departure_time"] else None,
                    )
                    for s in item["stops"]
                ]
                train = train_class(
                    item["train_id"], item["name"], carriages, stops)
                self._trains[train.train_id] = train
            except (NotFoundError, KeyError, TypeError, ValueError) as e:
                train_id = item.get("train_id", "<unknown>") if isinstance(item, dict) else "<unknown>"
                print(f"Error loading train {train_id}: {e}")

    def __str__(self):
        return f"TrainSim({len(self._trains)} trains, {self._rail_network})"
