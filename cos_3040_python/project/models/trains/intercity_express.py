from models.trains.helper.carriage import Carriage, CarriageType
from models.trains.intercity import IntercityTrain
from models.trains.helper.stop import Stop


class IntercityExpressTrain(IntercityTrain):
    def __init__(self, train_id: str, name: str, carriages: list, stops: list[Stop]):
        super().__init__(train_id, name, carriages, stops)

        self._reserved_seats = 0

    @property
    def reserved_seats(self):
        return self._reserved_seats

    @property
    def available_seats(self):
        return self.capacity - self.reserved_seats

    def reserve_seats(self, seats: int = 1):
        self._reserved_seats += seats