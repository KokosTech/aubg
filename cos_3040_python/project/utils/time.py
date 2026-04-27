"""Defines a simple time model and time conversion helpers."""

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
        """To minutes.
        Parameters:
            None
        Returns:
            int: Return value.
        """
        return self.hour * 60 + self.minute

    @staticmethod
    def minutes_to_time(minutes: int) -> Time:
        """Minutes to time.
        Parameters:
            minutes (int): minutes value.
        Returns:
            Time: Return value.
        """
        if minutes < 0:
            raise ValueError("minutes must be non-negative")

        return Time(minutes // 60 % 24, minutes % 60)

    @staticmethod
    def time_to_minutes(time: Time) -> int:
        """Time to minutes.
        Parameters:
            time (Time): time value.
        Returns:
            int: Return value.
        """
        return time.to_minutes

    @staticmethod
    def time_diff_minutes(self, other: Time) -> int:
        """Time diff minutes.
        Parameters:
            other (Time): other value.
        Returns:
            int: Return value.
        """
        if not isinstance(self, Time):
            raise TypeError("self must be a Time instance")
        if not isinstance(other, Time):
            raise TypeError("other must be a Time instance")
        diff = self.time_to_minutes(other) - self.time_to_minutes(self)
        if diff < 0:
            diff += 24 * 60
        return diff

    @staticmethod
    def time_to_str(time: Time | tuple[int, int] | None):
        """Time to str.
        Parameters:
            time (Time | tuple[int, int] | None): time value.
        Returns:
            None: Return value.
        """
        if isinstance(time, tuple):
            return f"{time[0]:02d}:{time[1]:02d}" if time else "N/A"

        return time.__str__() if time else "N/A"

    @staticmethod
    def minutes_to_str(minutes: int):
        """Minutes to str.
        Parameters:
            minutes (int): minutes value.
        Returns:
            None: Return value.
        """
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
