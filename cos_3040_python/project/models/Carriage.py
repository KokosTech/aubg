from enum import Enum

from utils.config import DEFAULT_CARRIAGE_CAPACITY


class CarriageType(Enum):
    SLEEPER = "sleeper"
    CLASS2 = "2nd class"
    CLASS1 = "1st class"
    BISTRO = "bistro"
    QUIET = "quiet"
    BIKE = "bike"


class Carriage:
    def __init__(
        self,
        carriage_type: CarriageType,
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
        return self._carriage_type

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("capacity must be a positive integer")
        self._capacity = value

    def __str__(self):
        return f"Carriage ({self._carriage_type.value}, capacity: {self._capacity})"

    def __repr__(self):
        return (
            f"carriage_type={self._carriage_type!r}, "
            f"capacity={self._capacity!r})")
