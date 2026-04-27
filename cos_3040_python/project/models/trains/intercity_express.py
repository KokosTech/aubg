"""Defines intercity express train behavior and carriage rules."""

from models.trains.helper.carriage import CarriageType
from models.trains.helper.stop import Stop
from models.trains.intercity import IntercityTrain


class IntercityExpressTrain(IntercityTrain):
    def __init__(self, train_id: str, name: str, carriages: list, stops: list[Stop]):
        super().__init__(train_id, name, carriages, stops)

        # bistro is mandatory for intercity express
        if carriages:
            if not any(c.carriage_type == CarriageType.BISTRO for c in self._carriages):
                raise ValueError("Intercity Express train must have a bistro carriage")

        self._reserved_seats = 0

    @property
    def reserved_seats(self):
        """Reserved seats.
        Parameters:
            None
        Returns:
            None: Return value.
        """
        return self._reserved_seats

    @property
    def available_seats(self):
        """Available seats.
        Parameters:
            None
        Returns:
            None: Return value.
        """
        return self.capacity - self.reserved_seats

    def reserve_seats(self, seats: int = 1):
        """Reserve seats.
        Parameters:
            seats (int): seats value.
        Returns:
            None: Return value.
        """
        if not isinstance(seats, int) or seats <= 0:
            raise ValueError("seats must be a positive integer")
        if self._reserved_seats + seats > self.capacity:
            raise ValueError("Cannot reserve more seats than train capacity")
        self._reserved_seats += seats

    def __str__(self):
        return f"[Intercity Express] {self._name} ({self._train_id})"
