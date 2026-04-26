import re
from abc import ABC, abstractmethod

from errors.custom_exceptions import NotFoundError
from models.trains.helper.carriage import Carriage
from models.trains.helper.stop import Stop
from utils.time import Time


class BaseTrain(ABC):
    def __init__(self, train_id: str, name: str, carriages: list, stops: list[Stop]):
        if not (isinstance(train_id, str) and re.match(r"[A-Z]{2}-\d{4,5}", train_id)):
            raise ValueError(
                "train_id must be in format 'AA-XXXX[X]' where AA are 2 uppercase letters and XXXX[X] is a 4-5 digit number")
        self._train_id = train_id

        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        self._name = name

        if not isinstance(carriages, list) or not all(isinstance(carriage, Carriage) for carriage in carriages):
            raise ValueError("carriages must be a list of Carriage objects")
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

    @property
    def capacity(self):
        return sum(c.capacity for c in self._carriages)

    @property
    def duration(self):
        if not self._stops or len(self.stops) < 2:
            return 0

        return self.get_time_length_from_to(self.stops[0].station.name, self.stops[-1].station.name)

    # abstract as adding a carriage depends on the type of train
    @abstractmethod
    def add_carriage(self, carriage):
        pass

    def append_stop(self, stop: Stop, duration: int):
        if not isinstance(stop, Stop):
            raise TypeError("stop must be a Stop instance")

        # if not the first stop, arrival_time is required
        if len(self._stops) > 0 and stop.arrival_time is None:
            raise ValueError(
                "arrival_time is required for all stops except the first")

        # if it is the first stop, departure_time is required
        if len(self._stops) == 0 and stop.departure_time is None:
            raise ValueError("departure_time is required for the first stop")

        # arrival must be before departure at the same stop
        if stop.arrival_time and stop.departure_time:
            if not Stop.check_validity(stop):
                raise ValueError(
                    "arrival_time must be before departure_time at the same stop")

        # new stop must be chronologically after the previous one
        if self._stops:
            prev = self._stops[-1]

            if prev.departure_time is None:
                prev.departure_time = prev.arrival_time + duration

            if not Stop.check_compatibility(prev, stop):
                raise ValueError(
                    f"Stop at '{stop.station.name}' must arrive after previous stop "
                    f"departs at {prev.departure_time}"
                )

        self._stops.append(stop)

    def remove_carriage(self, carriage):
        if carriage in self._carriages:
            self._carriages.remove(carriage)
            return
        raise NotFoundError(f"Carriage {carriage} not found")

    def get_time_length_from_to(self, from_station: str | None = None, to_station: str | None = None) -> int:
        if len(self._stops) < 2:
            return 0

        if from_station is None:
            from_station = self._stops[0].station.name

        if to_station is None:
            to_station = self._stops[-1].station.name

        def get_stop(name: str) -> Stop:
            stop = list(filter(lambda s: s.station.name == name, self._stops))
            if len(stop) != 1:
                raise NotFoundError("from_station must be in the train's stops")

            return stop[0]

        from_stop = get_stop(from_station)
        to_stop = get_stop(to_station)

        if not Stop.check_compatibility(from_stop, to_stop):
            raise ValueError(
                f"from_station must arrive after previous stop departs at {from_stop.departure_time}")

        from_minutes = from_stop.departure_time.to_minutes
        to_minutes = to_stop.arrival_time.to_minutes

        # this should never happen
        if to_minutes < from_minutes:
            raise ValueError(
                "to_station must be after from_station in the schedule")

        return to_minutes - from_minutes

    def display_carriages(self):
        if not self._carriages:
            print(f"No carriages on {self._name} ({self._train_id})")
            return

        print(f"Carriages on {self._name} ({self._train_id}):")
        for c in self._carriages:
            print(f"  - {c}")

    def display_stops(self):
        if not self._stops:
            print(f"No stops on {self._name} ({self._train_id})")
            return

        print(
            f"Stops on {self._name} ({self._train_id}) ({Time.minutes_to_str(self.get_time_length_from_to())}):")
        for s in self.stops:
            print(f"  - {s}")

    def __lt__(self, other):
        if not isinstance(other, BaseTrain):
            return NotImplemented

        return self.stops[0].departure_time < other.stops[0].departure_time

    def __gt__(self, other):
        if not isinstance(other, BaseTrain):
            return NotImplemented

        return self.stops[0].departure_time > other.stops[0].departure_time

    def __str__(self):
        return f"{self._name} ({self._train_id})"
