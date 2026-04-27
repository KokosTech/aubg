"""Defines available train carriage types."""

from enum import Enum


class CarriageType(Enum):
    SLEEPER = "sleeper"
    CLASS2 = "2nd class"
    CLASS1 = "1st class"
    BISTRO = "bistro"
    QUIET = "quiet"
    BIKE = "bike"
