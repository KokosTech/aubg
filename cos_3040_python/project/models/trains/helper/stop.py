from dataclasses import dataclass

from models.rail.train_station import TrainStation
from utils.time import Time


@dataclass
class Stop:
    station: TrainStation
    arrival_time: Time | None
    departure_time: Time | None

    @staticmethod
    def check_validity(other: Stop) -> bool:
        if other.arrival_time is None or other.departure_time is None:
            return False

        return other.arrival_time <= other.departure_time

    def __str__(self) -> str:
        return f"{self.station.name}: {' - '.join(filter(lambda x: x != 'N/A', [self.arrival_time.__str__(), self.departure_time.__str__()]))}"
