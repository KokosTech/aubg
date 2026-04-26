"""Module containing the PassengerTrain class, a concrete implementation of BaseTrain."""

from models.trains.base import BaseTrain
from models.trains.helper.carriage import Carriage, CarriageType
from models.trains.helper.stop import Stop


class PassengerTrain(BaseTrain):
    def __init__(self, train_id: str, name: str, carriages: list, stops: list[Stop]):
        super().__init__(train_id, name, carriages, stops)

    # you could have any carriage type from the constructor, but only allow certain types to be added later
    def add_carriage(self, carriage: Carriage):
        if not isinstance(carriage, Carriage):
            raise TypeError("carriage must be a Carriage instance")

        if carriage.carriage_type not in {CarriageType.CLASS2, CarriageType.BIKE, CarriageType.QUIET}:
            raise ValueError(
                f"PassengerTrain can only have 2nd class, bike, or quiet carriages, got {carriage.carriage_type.value}"
            )

        self._carriages.append(carriage)

    def get_journey_info(self) -> str:
        if not self._stops:
            return f"{self._name} ({self._train_id}) — no stops scheduled"

        first = self._stops[0]
        last = self._stops[-1]

        return (
            f"{self._name} ({self._train_id}) | "
            f"From: {first.station.name} at {first.departure_time.__str__()}, → "
            f"To: {last.station.name} at {last.arrival_time.__str__()} | "
            f"Stops: {len(self._stops)} | "
            f"Capacity: {self.capacity}"
        )

    def __str__(self):
        return f"[Passenger] {self._name} ({self._train_id})"
