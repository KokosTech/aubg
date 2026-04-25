from dataclasses import dataclass

from models.rail.train_station import TrainStation
from utils.time_to_str import time_to_str


@dataclass
class Stop:
    station: TrainStation
    arrival_time: tuple[int, int] | None
    departure_time: tuple[int, int] | None

    def __str__(self):
        return f"{self.station.name}: {' - '.join(filter(lambda x: x != 'N/A', [time_to_str(self.arrival_time), time_to_str(self.departure_time)]))}"
