import json

from models.rail.track import Track
from models.rail.train_station import TrainStation


class RailNetwork:
    def __init__(self):
        self._stations: dict[str, TrainStation] = {}
        self._tracks: list[Track] = []

    @property
    def stations(self):
        return self._stations

    @property
    def tracks(self):
        return self._tracks

    def create_station(self, name: str) -> TrainStation:
        station = TrainStation(name)
        self._stations[station.name] = station
        return station

    def remove_station(self, name: str):
        if name not in self._stations:
            raise ValueError(f"Station with name '{name}' not found")
        self._stations.pop(name)
        self._tracks = [
            t for t in self._tracks
            if t.from_station_id != name and t.to_station_id != name
        ]

    def get_station(self, name: str) -> TrainStation:
        if name not in self._stations:
            raise ValueError(f"Station with name '{name}' not found")
        return self._stations[name]

    def create_track(self, from_station: str, to_station: str, distance_km: float, max_speed_kmh: int) -> Track:
        if from_station not in self._stations:
            raise ValueError(f"Station '{from_station}' not found")
        if to_station not in self._stations:
            raise ValueError(f"Station '{to_station}' not found")
        if any(t.from_station_id == from_station and t.to_station_id == to_station for t in self._tracks):
            raise ValueError(
                f"Track from '{from_station}' to '{to_station}' already exists")

        track = Track(from_station, to_station, distance_km, max_speed_kmh)
        self._tracks.append(track)
        return track

    def remove_track(self, from_station: str, to_station: str):
        for track in self._tracks:
            if track.from_station_id == from_station and track.to_station_id == to_station:
                self._tracks.remove(track)
                return
        raise ValueError(f"Track from '{from_station}' to '{to_station}' not found")

    def get_tracks_from(self, station: str) -> list[Track]:
        return [t for t in self._tracks if t.from_station_id == station]
    
    def get_track(self, from_station: str, to_station: str) -> Track:
        for track in self._tracks:
            if track.from_station_id == from_station and track.to_station_id == to_station:
                return track
        raise ValueError(f"Track from '{from_station}' to '{to_station}' not found")

    def display_network(self):
        print("=== Rail Network ===")
        print("Stations:")
        for station in self._stations.values():
            print(f"  - {station}")
        print("Tracks:")
        for track in self._tracks:
            print(
                f"  - {track.from_station_id} → {track.to_station_id} | "
                f"{track.distance_km} km @ max {track.max_speed_kmh} km/h"
            )
            
    def save_to_json(self, filename: str):
        data = {
            "stations": [s.name for s in self._stations.values()],
            "tracks": [
                {
                    "from": t.from_station_id,
                    "to": t.to_station_id,
                    "distance_km": t.distance_km,
                    "max_speed_kmh": t.max_speed_kmh
                }
                for t in self._tracks
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            
    def load_from_json(self, filename: str):
        self._stations.clear()
        self._tracks.clear()
        
        with open(filename, 'r') as f:
            data = json.load(f)
        self._stations = {name: TrainStation(name) for name in data["stations"]}
        self._tracks = [
            Track(
                from_station_id=t["from"],
                to_station_id=t["to"],
                distance_km=t["distance_km"],
                max_speed_kmh=t["max_speed_kmh"]
            )
            for t in data["tracks"]
        ]

    def __str__(self):
        return f"RailNetwork({len(self._stations)} stations, {len(self._tracks)} tracks)"
