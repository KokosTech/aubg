from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Time:
    hour: int
    minute: int

    def __post_init__(self):
        if not (0 <= self.hour < 24):
            raise ValueError("hour must be 0–23")
        if not (0 <= self.minute < 60):
            overflow = self.minute // 60
            self.hour = (self.hour + overflow) % 24
            self.minute %= 60

    @property
    def to_minutes(self) -> int:
        return self.hour * 60 + self.minute

    @staticmethod
    def minutes_to_time(minutes: int) -> Time:
        if minutes < 0:
            raise ValueError("minutes must be non-negative")

        return Time(minutes // 60 % 24, minutes % 60)

    @staticmethod
    def time_to_minutes(time: Time) -> int:
        return time.to_minutes

    @staticmethod
    def time_diff_minutes(self, other: Time) -> int:
        if not isinstance(other, Time):
            raise TypeError("other must be a Time instance")
        return self.time_to_minutes(other) - self.time_to_minutes(self)

    @staticmethod
    def time_to_str(time: Time | tuple[int, int] | None):
        if isinstance(time, tuple):
            return f"{time[0]:02d}:{time[1]:02d}" if time else "N/A"

        return time.__str__() if time else "N/A"

    @staticmethod
    def minutes_to_str(minutes: int):
        hours = minutes // 60
        mins = minutes % 60
        return Time.time_to_str((hours, mins))

    def __add__(self, other: int) -> Time:
        if not isinstance(other, int):
            raise TypeError("other must be an integer")
        return Time(self.hour, self.minute + other)

    def __lt__(self, other: Time) -> bool:
        if not isinstance(other, Time):
            return NotImplemented
        return self.hour < other.hour or (self.hour == other.hour and self.minute < other.minute)

    def __le__(self, other: Time) -> bool:
        if not isinstance(other, Time):
            return NotImplemented
        return self.hour < other.hour or (self.hour == other.hour and self.minute <= other.minute)

    def __gt__(self, other: Time) -> bool:
        if not isinstance(other, Time):
            return NotImplemented
        return self.hour > other.hour or (self.hour == other.hour and self.minute > other.minute)

    def __ge__(self, other: Time) -> bool:
        if not isinstance(other, Time):
            return NotImplemented
        return self.hour > other.hour or (self.hour == other.hour and self.minute >= other.minute)

    def __eq__(self, other: Time) -> bool:
        if not isinstance(other, Time):
            return NotImplemented
        return self.hour == other.hour and self.minute == other.minute

    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"
