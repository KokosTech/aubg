from dataclasses import dataclass


@dataclass
class Time:
    hour: int
    minute: int

    def __post_init__(self):
        if not (0 <= self.hour < 24):
            raise ValueError("hour must be 0–23")
        if not (0 <= self.minute < 60):
            raise ValueError("minute must be 0–59")

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
        return time.hour * 60 + time.minute

    @staticmethod
    def time_diff_minutes(self, other: Time) -> int:
        if not isinstance(other, Time):
            raise TypeError("other must be a Time instance")
        return self.time_to_minutes(other) - self.time_to_minutes(self)

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
