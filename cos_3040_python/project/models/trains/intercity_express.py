from models.trains.helper.carriage import CarriageType
from models.trains.intercity import IntercityTrain
from models.trains.helper.stop import Stop


class IntercityExpressTrain(IntercityTrain):
    def __init__(self, train_id: str, name: str, carriages: list, stops: list[Stop]):
        super().__init__(train_id, name, carriages, stops)

        # bistro is mandatory for intercity express
        for carriage in self.carriages:
            if carriage.carriage_type != CarriageType.BISTRO:
                raise ValueError(
                    "Intercity Express trains must have a Bistro carriage")

        self._reserved_seats = 0

    @property
    def reserved_seats(self):
        return self._reserved_seats

    @property
    def available_seats(self):
        return self.capacity - self.reserved_seats

    def reserve_seats(self, seats: int = 1):
        self._reserved_seats += seats

    def __str__(self):
        return f"[Intercity Express] {self._name} ({self._train_id})"
