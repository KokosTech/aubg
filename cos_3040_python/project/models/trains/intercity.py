from models.trains.helper.carriage import Carriage, CarriageType
from models.trains.helper.stop import Stop
from models.trains.passenger import PassengerTrain


class IntercityTrain(PassengerTrain):
    def __init__(self, train_id: str, name: str, carriages: list, stops: list[Stop]):
        super().__init__(train_id, name, carriages, stops)

    def add_carriage(self, carriage):
        if not isinstance(carriage, Carriage):
            raise TypeError("carriage must be a Carriage instance")

        if carriage.carriage_type not in {CarriageType.CLASS1, CarriageType.CLASS2, CarriageType.BIKE, CarriageType.QUIET, CarriageType.BISTRO, CarriageType.SLEEPER}:
            raise ValueError(
                f"IntercityTrain can only have 1st class, 2nd class, bike, or quiet carriages, got {carriage.carriage_type.value}"
            )

        self._carriages.append(carriage)
        
    @property
    def has_bistro(self):
        return any(c.carriage_type == CarriageType.BISTRO for c in self._carriages)