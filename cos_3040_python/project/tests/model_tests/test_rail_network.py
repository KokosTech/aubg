"""Tests rail network station and track behavior."""

import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout

from errors.custom_exceptions import NotFoundError
from models.rail.rail_network import RailNetwork


class TestRailNetwork(unittest.TestCase):
    def setUp(self):
        self.network = RailNetwork()
        self.network.create_station("Sofia")
        self.network.create_station("Plovdiv")
        self.network.create_station("Burgas")

    def test_create_track_and_get_track(self):
        track = self.network.create_track("Sofia", "Plovdiv", 150.0, 120)
        fetched = self.network.get_track("Sofia", "Plovdiv")
        self.assertIs(track, fetched)

    def test_create_track_rejects_duplicate_direction(self):
        self.network.create_track("Sofia", "Plovdiv", 150.0, 120)
        with self.assertRaises(ValueError):
            self.network.create_track("Sofia", "Plovdiv", 151.0, 120)

    def test_rename_station_updates_track_endpoints(self):
        self.network.create_track("Sofia", "Plovdiv", 150.0, 120)
        self.network.rename_station("Sofia", "Sofia West")

        self.assertIn("Sofia West", self.network.stations)
        self.assertNotIn("Sofia", self.network.stations)
        self.assertIsNotNone(self.network.get_track("Sofia West", "Plovdiv"))

    def test_remove_station_removes_connected_tracks(self):
        self.network.create_track("Sofia", "Plovdiv", 150.0, 120)
        self.network.create_track("Plovdiv", "Burgas", 250.0, 110)

        self.network.remove_station("Plovdiv")
        self.assertNotIn("Plovdiv", self.network.stations)
        self.assertEqual(len(self.network.tracks), 0)
        self.assertIsNone(self.network.get_track("Sofia", "Plovdiv"))
        self.assertIsNone(self.network.get_track("Plovdiv", "Burgas"))
        self.assertEqual(len(self.network.get_tracks_from("Sofia")), 0)

    def test_get_station_raises_for_missing(self):
        with self.assertRaises(NotFoundError):
            self.network.get_station("Missing")

    def test_save_and_load_round_trip(self):
        # using dummy temporary file
        self.network.create_track("Sofia", "Plovdiv", 150.0, 120)
        fd, path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        try:
            self.network.save_to_json(path)
            other = RailNetwork()
            other.load_from_json(path)
            self.assertCountEqual(other.stations.keys(), ["Sofia", "Plovdiv", "Burgas"])
            loaded = other.get_track("Sofia", "Plovdiv")
            self.assertIsNotNone(loaded)
            self.assertEqual(loaded.max_speed_kmh, 120)
        finally:
            os.remove(path)

    def test_load_invalid_json_missing_keys_keeps_empty(self):
        fd, path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        try:
            with open(path, "w") as handle:
                json.dump({"stations": ["A"]}, handle)

            other = RailNetwork()
            # so it doesnt pollute tests output
            with io.StringIO() as buf, redirect_stdout(buf):
                other.load_from_json(path)
            self.assertEqual(len(other.stations), 0)
            self.assertEqual(len(other.tracks), 0)
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
