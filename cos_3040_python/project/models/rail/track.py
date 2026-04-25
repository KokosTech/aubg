from dataclasses import dataclass


@dataclass
class Track:
    from_station_id: str
    to_station_id: str
    distance_km: float
    max_speed_kmh: int
