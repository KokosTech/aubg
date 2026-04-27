"""Defines rail tracks connecting train stations."""

from dataclasses import dataclass


@dataclass
class Track:
    from_station_id: str
    to_station_id: str
    distance_km: float
    max_speed_kmh: int

    # there are no checks for consistency, as it is assumed that the network is already validated

    def __str__(self):
        return f"{self.from_station_id} → {self.to_station_id} | {self.distance_km} km @ max {self.max_speed_kmh} km/h"
