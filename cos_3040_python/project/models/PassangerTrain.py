"""Module containing the PassengerTrain class, a concrete implementation of BaseTrain."""

from models.BaseTrain import BaseTrain
from models.Carriage import Carriage, CarriageType


class PassengerTrain(BaseTrain):
    def add_carriage(self, carriage: Carriage):
        if not isinstance(carriage, Carriage):
            raise TypeError("carriage must be a Carriage instance")
        self._carriages.append(carriage)

    def get_journey_info(self) -> str:
        if not self._stops:
            return f"{self._name} ({self._train_id}) — no stops scheduled"

        first = self._stops[0]
        last = self._stops[-1]
        
        def format_time(time_tuple):
            """Format (hour, minute) tuple to 'HH:MM' string, or 'N/A' if None."""
            return f"{time_tuple[0]:02d}:{time_tuple[1]:02d}" if time_tuple else "N/A"
        
        return (
            f"{self._name} ({self._train_id}) | "
            f"From: {first.station.name} at {format_time(first.departure_time)} → "
            f"To: {last.station.name} at {format_time(last.arrival_time)} | "
            f"Stops: {len(self._stops)} | "
            f"Capacity: {self.capacity()}"
        )

    def __str__(self):
        return f"[Passenger] {self._name} ({self._train_id})"
