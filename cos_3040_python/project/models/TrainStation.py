import re
import uuid


class TrainStation:
    def __init__(self, name: str):
        if not isinstance(name, str) or not re.match(r"^[A-Za-z\s]+$", name):
            raise ValueError("name must be a non-empty string containing only letters and spaces")

        self._name = name

    # Names are Unique Identifiers for Train Stations
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not re.match(r"^[A-Za-z\s]+$", value):
            raise ValueError("name must be a non-empty string containing only letters and spaces")

        self._name = value

    def __str__(self):
        return f"{self._name}"