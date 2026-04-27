"""Manages train stations, tracks, and rail network persistence."""

import json

from errors.custom_exceptions import NotFoundError
from models.rail.track import Track
from models.rail.train_station import TrainStation


class RailNetwork:
    def __init__(self):
        self._stations: dict[str, TrainStation] = {}
        self._tracks: list[Track] = []

    @property
    def stations(self) -> dict[str, TrainStation]:
        """Stations value.
        Parameters:
            None
        Returns:
            dict[str, TrainStation]: Return value.
        """
        return self._stations

    @property
    def tracks(self) -> list[Track]:
        """Tracks value.
        Parameters:
            None
        Returns:
            list[Track]: Return value.
        """
        return self._tracks

    def create_station(self, name: str) -> TrainStation:
        """Create station.
        Parameters:
            name (str): name value.
        Returns:
            TrainStation: Return value.
        """
        station = TrainStation(name)
        self._stations[station.name] = station
        return station

    def remove_station(self, name: str):
        """Remove station.
        Parameters:
            name (str): name value.
        Returns:
            None: Return value.
        """
        if name not in self._stations:
            raise NotFoundError(f"Station '{name}' not found")

        self._stations.pop(name)
        self._tracks = [
            t for t in self._tracks
            if t.from_station_id != name and t.to_station_id != name
        ]

    def get_station(self, name: str) -> TrainStation:
        """Get station.
        Parameters:
            name (str): name value.
        Returns:
            TrainStation: Return value.
        """
        if name not in self._stations:
            raise NotFoundError(f"Station '{name}' not found")
        return self._stations[name]

    def rename_station(self, old_name: str, new_name: str) -> TrainStation:
        """Rename station.
        Parameters:
            old_name (str): old_name value.
            new_name (str): new_name value.
        Returns:
            TrainStation: Return value.
        """
        if old_name not in self._stations:
            raise NotFoundError(f"Station '{old_name}' not found")
        if new_name in self._stations and new_name != old_name:
            raise ValueError(f"Station '{new_name}' already exists")

        station = self._stations.pop(old_name)
        station.name = new_name
        self._stations[new_name] = station

        for track in self._tracks:
            if track.from_station_id == old_name:
                track.from_station_id = new_name
            if track.to_station_id == old_name:
                track.to_station_id = new_name

        return station

    def create_track(self, from_station: str, to_station: str, distance_km: float, max_speed_kmh: int) -> Track:
        """Create track.
        Parameters:
            from_station (str): from_station value.
            to_station (str): to_station value.
            distance_km (float): distance_km value.
            max_speed_kmh (int): max_speed_kmh value.
        Returns:
            Track: Return value.
        """
        if from_station not in self._stations:
            raise NotFoundError(f"Station '{from_station}' not found")
        if to_station not in self._stations:
            raise NotFoundError(f"Station '{to_station}' not found")
        if from_station == to_station:
            raise ValueError("from_station and to_station must be different")
        if distance_km <= 0:
            raise ValueError("distance_km must be positive")
        if max_speed_kmh <= 0:
            raise ValueError("max_speed_kmh must be positive")

        # for algorithm simplicity, it is allowed to only have 1 track between 2 stations in a direction
        if any(t.from_station_id == from_station and t.to_station_id == to_station for t in self._tracks):
            raise ValueError(
                f"Track from '{from_station}' to '{to_station}' already exists")

        track = Track(from_station, to_station, distance_km, max_speed_kmh)
        self._tracks.append(track)
        return track

    def remove_track(self, from_station: str, to_station: str):
        """Remove track.
        Parameters:
            from_station (str): from_station value.
            to_station (str): to_station value.
        Returns:
            None: Return value.
        """
        for track in self._tracks:
            if track.from_station_id == from_station and track.to_station_id == to_station:
                self._tracks.remove(track)
                return
        raise NotFoundError(f"Track from '{from_station}' to '{to_station}' not found")

    def get_tracks_from(self, station: str) -> list[Track]:
        """Get tracks from.
        Parameters:
            station (str): station value.
        Returns:
            list[Track]: Return value.
        """
        return [t for t in self._tracks if t.from_station_id == station]

    def get_track(self, from_station: str, to_station: str) -> Track | None:
        """Get track.
        Parameters:
            from_station (str): from_station value.
            to_station (str): to_station value.
        Returns:
            Track | None: Return value.
        """
        for track in self._tracks:
            if track.from_station_id == from_station and track.to_station_id == to_station:
                return track
        return None

    def display_network(self):
        """Display network.
        Parameters:
            None
        Returns:
            None: Return value.
        """
        print("=== Rail Network ===")
        print("Stations:")
        for station in self._stations.values():
            print(f"  - {station}")
        print("Tracks:")
        for track in self._tracks:
            print(f"  - {track}")

    def save_to_json(self, filename: str):
        """Save to json.
        Parameters:
            filename (str): filename value.
        Returns:
            None: Return value.
        """
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

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving to {filename}: {e}")

    def load_from_json(self, filename: str):
        """Load from json.
        Parameters:
            filename (str): filename value.
        Returns:
            None: Return value.
        """
        self._stations.clear()
        self._tracks.clear()
        data = dict()

        try:
            with open(filename, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, IOError) as e:
            print(f"Continuing with empty network. Error loading from {filename}: {e}")
            raise

        if not all(key in data for key in ("stations", "tracks")):
            print("Invalid JSON format. Missing required keys. Continuing with empty network.")
            return

        try:
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
        except KeyError as e:
            print(f"Invalid JSON format. Missing key: {e}. Continuing with empty network.")
            return

    def __str__(self):
        return f"RailNetwork ({len(self._stations)} stations, {len(self._tracks)} tracks)"
