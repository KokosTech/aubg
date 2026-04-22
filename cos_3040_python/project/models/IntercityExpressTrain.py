from models.Carriage import Carriage, CarriageType
from models.IntercityTrain import IntercityTrain
from models.Stop import Stop


class IntercityExpressTrain(IntercityTrain):
    def __init__(self, train_id: str, name: str, carriages: list, stops: list[Stop]):
        super().__init__(train_id, name, carriages, stops)
