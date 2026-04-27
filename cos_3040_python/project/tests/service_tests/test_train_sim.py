import json
import os
import tempfile
import unittest

from models.rail.rail_network import RailNetwork
from models.trains.helper.stop import Stop
from models.trains.passenger import PassengerTrain
from services.train_sim import TrainSim
from utils.time import Time


class TestTrainSim(unittest.TestCase):
    def setUp(self):
        self.network = RailNetwork()
        for name in ("Sofia", "Plovdiv", "Stara Zagora", "Burgas"):
            self.network.create_station(name)

        self.network.create_track("Sofia", "Plovdiv", 150.0, 150)
        self.network.create_track("Plovdiv", "Burgas", 250.0, 125)
        self.network.create_track("Sofia", "Stara Zagora", 220.0, 140)
        self.network.create_track("Stara Zagora", "Burgas", 180.0, 120)

        self.sim = TrainSim(self.network)

        direct_fast = PassengerTrain(
            "BV-1000",
            "Fast Direct",
            [],
            [
                Stop(self.network.get_station("Sofia"), None, Time(8, 0)),
                Stop(self.network.get_station("Burgas"), Time(11, 0), None),
            ],
        )
        direct_slow = PassengerTrain(
            "BV-1001",
            "Slow Direct",
            [],
            [
                Stop(self.network.get_station("Sofia"), None, Time(7, 50)),
                Stop(self.network.get_station("Burgas"), Time(11, 30), None),
            ],
        )
        transfer_leg1 = PassengerTrain(
            "BV-1002",
            "Via Plovdiv 1",
            [],
            [
                Stop(self.network.get_station("Sofia"), None, Time(8, 5)),
                Stop(self.network.get_station("Plovdiv"), Time(9, 20), Time(9, 22)),
            ],
        )
        transfer_leg2 = PassengerTrain(
            "BV-1003",
            "Via Plovdiv 2",
            [],
            [
                Stop(self.network.get_station("Plovdiv"), None, Time(9, 40)),
                Stop(self.network.get_station("Burgas"), Time(12, 0), None),
            ],
        )

        for train in (direct_fast, direct_slow, transfer_leg1, transfer_leg2):
            self.sim.add_train(train)

    def test_search_direct_only_returns_sorted_by_duration(self):
        results = self.sim.search_journeys("Sofia", "Burgas", direct_only=True, sort_by="duration")
        self.assertGreaterEqual(len(results), 2)
        self.assertEqual(results[0].legs[0].train_id, "BV-1000")

    def test_search_with_departure_filter(self):
        results = self.sim.search_journeys("Sofia", "Burgas", departure_time=Time(8, 0), direct_only=True)
        returned_ids = [journey.legs[0].train_id for journey in results]
        self.assertIn("BV-1000", returned_ids)
        self.assertNotIn("BV-1001", returned_ids)

    def test_station_and_track_usage_helpers(self):
        station_users = self.sim.get_trains_using_station("Plovdiv")
        self.assertCountEqual(station_users, ["BV-1002", "BV-1003"])

        track_users = self.sim.get_trains_using_track("Sofia", "Plovdiv")
        self.assertEqual(track_users, ["BV-1002"])

    def test_search_validates_station_inputs(self):
        with self.assertRaises(ValueError):
            self.sim.search_journeys("Missing", "Burgas")
        with self.assertRaises(ValueError):
            self.sim.search_journeys("Sofia", "Missing")
        with self.assertRaises(ValueError):
            self.sim.search_journeys("Sofia", "Sofia")

    def test_remove_trains_using_track(self):
        removed = self.sim.remove_trains_using_track("Sofia", "Plovdiv")
        self.assertEqual(removed, ["BV-1002"])
        self.assertNotIn("BV-1002", self.sim.trains)

    def test_remove_trains_using_station(self):
        removed = self.sim.remove_trains_using_station("Plovdiv")
        self.assertCountEqual(removed, ["BV-1002", "BV-1003"])
        self.assertNotIn("BV-1002", self.sim.trains)
        self.assertNotIn("BV-1003", self.sim.trains)

    def test_save_and_load_trains_round_trip(self):
        fd, path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        try:
            self.sim.save_trains_to_json(path)
            loaded = TrainSim(self.network)
            loaded.load_trains_from_json(path)
            self.assertEqual(set(loaded.trains.keys()), set(self.sim.trains.keys()))
        finally:
            os.remove(path)

    def test_load_rejects_non_list_root(self):
        fd, path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        try:
            with open(path, "w") as handle:
                json.dump({"not": "a list"}, handle)
            with self.assertRaises(ValueError):
                self.sim.load_trains_from_json(path)
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
