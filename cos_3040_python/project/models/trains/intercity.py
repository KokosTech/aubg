from models.trains.helper.carriage import Carriage, CarriageType
from models.trains.passenger import PassengerTrain


class IntercityTrain(PassengerTrain):
    ALLOWED_CARRIAGE_TYPES = {
        CarriageType.CLASS1,
        CarriageType.CLASS2,
        CarriageType.BIKE,
        CarriageType.QUIET,
        CarriageType.BISTRO,
        CarriageType.SLEEPER
    }

    def add_carriage(self, carriage: Carriage):
        if not isinstance(carriage, Carriage):
            raise TypeError("carriage must be a Carriage instance")

        if carriage.carriage_type not in self.ALLOWED_CARRIAGE_TYPES:
            raise ValueError(
                f"IntercityTrain can only have 1st class, 2nd class, bike, quiet, bistro, or sleeper carriages, got "
                f"{carriage.carriage_type.value}"
            )

        self._carriages.append(carriage)

    @property
    def has_bistro(self):
        return any(c.carriage_type == CarriageType.BISTRO for c in self._carriages)

    def serve_food(self):
        ...  # TODO

    def __str__(self):
        return f"[Intercity] {self._name} ({self._train_id})"
