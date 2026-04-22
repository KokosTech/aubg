from dataclasses import dataclass
from datetime import datetime


@dataclass
class Stop:
    station_id: str
    departure_time: datetime
