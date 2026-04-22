import re
from abc import ABC, abstractmethod

from models.Stop import Stop
from utils.time_to_str import minutes_to_str


class BaseTrain(ABC):
    def __init__(self, train_id: str, name: str, carriages: list, stops: list[Stop]):
        if not isinstance(train_id, str) or not re.match(r"[A-Z]{2}\-\d{4,5}", train_id):
            raise ValueError(
                "train_id must be in format 'AA-XXXX[X]' where AA are 2 uppercase letters and XXXX[X] is a 4-5 digit number")

        self._train_id = train_id

        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")

        self._name = name

        # todo: validate carriages with its class
        self._carriages = carriages

        if not isinstance(stops, list) or not all(isinstance(stop, Stop) for stop in stops):
            raise ValueError("stops must be a list of Stop objects")

        self._stops = stops

    @property
    def train_id(self):
        return self._train_id

    @property
    def name(self):
        return self._name

    @property
    def carriages(self):
        return self._carriages

    @property
    def stops(self):
        return self._stops

    # abstract as adding a carriage depends on the type of train
    @abstractmethod
    def add_carriage(self, carriage):
        pass


    def add_stop(self, stop: Stop):
        if not isinstance(stop, Stop):
            raise TypeError("stop must be a Stop instance")

        # if not the first stop, arrival_time is required
        if self._stops and stop.arrival_time is None:
            raise ValueError(
                "arrival_time is required for all stops except the first")

        # if it is the first stop, departure_time is required
        if not self._stops and stop.departure_time is None:
            raise ValueError("departure_time is required for the first stop")

        # arrival must be before departure at the same stop
        if stop.arrival_time and stop.departure_time:
            if stop.arrival_time >= stop.departure_time:
                raise ValueError(
                    "arrival_time must be before departure_time at the same stop")

        # new stop must be chronologically after the previous one
        if self._stops:
            prev = self._stops[-1]
            if prev.departure_time and stop.arrival_time:
                if stop.arrival_time <= prev.departure_time:
                    raise ValueError(
                        f"Stop at '{stop.station.name}' must arrive after previous stop "
                        f"departs at {prev.departure_time}"
                    )

        # mark previous last stop's departure as required now
        if self._stops:
            prev = self._stops[-1]
            if prev.departure_time is None:
                raise ValueError(
                    f"Previous stop '{prev.station.name}' has no departure_time — "
                    "only the last stop can have no departure_time"
                )

        self._stops.append(stop)
            

    def remove_carriage(self, carriage):
        if carriage in self._carriages:
            self._carriages.remove(carriage)

    @property
    def capacity(self):
        return sum(c.capacity for c in self._carriages)

    def get_time_length_from_to(self, from_station: str | None = None, to_station: str | None = None) -> int:
        # check if stations are in stops dont use next()
        if from_station is None:
            from_station = self._stops[0].station.name
            
        if to_station is None:
            to_station = self._stops[-1].station.name
    
        from_stop = list(filter(lambda s: s.station.name == from_station, self._stops))
        if len(from_stop) != 1:
            raise ValueError("from_station must be in the train's stops")

        to_stop = list(filter(lambda s: s.station.name == to_station, self._stops))
        if len(to_stop) != 1:
            raise ValueError("to_station must be in the train's stops")

        if not from_stop[0].departure_time or not to_stop[0].arrival_time:
            raise ValueError("Both stops must have departure and arrival times respectively")

        from_minutes = from_stop[0].departure_time[0] * 60 + from_stop[0].departure_time[1]
        to_minutes = to_stop[0].arrival_time[0] * 60 + to_stop[0].arrival_time[1]

        if to_minutes < from_minutes:
            raise ValueError("to_station must be after from_station in the schedule")

        return to_minutes - from_minutes

    def display_carriages(self):
        print(f"Carriages on {self._name} ({self._train_id}):")
        for c in self._carriages:
            print(f"  - {c}")

    def display_stops(self):
        print(f"Stops on {self._name} ({self._train_id}) ({minutes_to_str(self.get_time_length_from_to())}):")
        for s in self._stops:
            print(f"  - {s}")

    def __lt__(self, other):
        return self._stops[0].departure_time < other._stops[0].departure_time

    def __gt__(self, other):
        return self._stops[0].departure_time > other._stops[0].departure_time

    def __str__(self):
        return f"{self._name} ({self._train_id})"
