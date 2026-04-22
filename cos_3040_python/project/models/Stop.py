from dataclasses import dataclass

from models.TrainStation import TrainStation


@dataclass
class Stop:
    station: TrainStation
    arrival_time: tuple[int, int] | None
    departure_time: tuple[int, int] | None
