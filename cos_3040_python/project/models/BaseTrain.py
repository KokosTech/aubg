import re
from abc import ABC, abstractmethod

from models.Stop import Stop


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

    def add_stop(self, stop):
        if not isinstance(stop, Stop):
            raise ValueError("stop must be a Stop object")
        
        for s in self._stops:
            if s.n == stop.station_name:
                raise ValueError(f"Stop with station name '{stop.station_name}' already exists")
            

    def remove_carriage(self, carriage):
        if carriage in self._carriages:
            self._carriages.remove(carriage)

    def capacity(self):
        return sum(c.capacity for c in self._carriages)

    def display_carriages(self):
        return [str(c) for c in self._carriages]

    def display_stops(self):
        return [str(s) for s in self._stops]

    def __lt__(self, other):
        return self._stops[0].departure_time < other._stops[0].departure_time

    def __gt__(self, other):
        return self._stops[0].departure_time > other._stops[0].departure_time

    def __str__(self):
        return f"{self._name} ({self._train_id})"
