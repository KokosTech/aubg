from models.trains.helper.carriage import Carriage, CarriageType
from models.trains.intercity import IntercityTrain
from models.trains.helper.stop import Stop


class IntercityExpressTrain(IntercityTrain):
    def __init__(self, train_id: str, name: str, carriages: list, stops: list[Stop]):
        super().__init__(train_id, name, carriages, stops)
