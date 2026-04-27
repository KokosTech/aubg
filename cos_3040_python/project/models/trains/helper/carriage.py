"""Defines train carriages and carriage capacity validation."""

from models.trains.helper.carriage_types import CarriageType
from utils.config import DEFAULT_CARRIAGE_CAPACITY


class Carriage:
    def __init__(
        self,
        carriage_type: CarriageType = CarriageType.CLASS2,
        capacity: int = DEFAULT_CARRIAGE_CAPACITY
    ):
        if not isinstance(carriage_type, CarriageType):
            raise ValueError(
                f"carriage_type must be a CarriageType, got {type(carriage_type)}")
        self._carriage_type = carriage_type

        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self._capacity = capacity

    @property
    def carriage_type(self):
        """Carriage type.
        Parameters:
            None
        Returns:
            None: Return value.
        """
        return self._carriage_type

    @property
    def capacity(self):
        """Capacity value.
        Parameters:
            None
        Returns:
            None: Return value.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        """Capacity value.
        Parameters:
            value (int): value value.
        Returns:
            None: Return value.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("capacity must be a positive integer")
        self._capacity = value

    def __str__(self):
        return f"{self._carriage_type.value.capitalize()} carriage ({self._capacity} seats)"
