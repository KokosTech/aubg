"""Tests train creation and schedule validation behavior."""

import unittest

from models.rail.rail_network import RailNetwork
from models.trains.helper.carriage import Carriage
from models.trains.helper.carriage_types import CarriageType
from models.trains.helper.stop import Stop
from models.trains.intercity_express import IntercityExpressTrain
from models.trains.passenger import PassengerTrain
from services.validate_train_schedule import validate_train_schedule
from utils.time import Time


class TestTrainModelsAndSchedule(unittest.TestCase):
    def setUp(self):
        self.network = RailNetwork()
        self.network.create_station("Sofia")
        self.network.create_station("Plovdiv")
        self.network.create_station("Burgas")
        self.network.create_track("Sofia", "Plovdiv", 150.0, 150)
        self.network.create_track("Plovdiv", "Burgas", 250.0, 125)

    def test_carriage_validates_positive_capacity(self):
        with self.assertRaises(ValueError):
            Carriage(CarriageType.CLASS2, 0)

    def test_passenger_train_rejects_non_carriage_items(self):
        with self.assertRaises(ValueError):
            PassengerTrain("BV-1234", "Bad", [object()], [])

    def test_append_stop_accepts_valid_sequence(self):
        train = PassengerTrain("BV-1234", "Valid", [], [])
        train.append_stop(Stop(self.network.get_station("Sofia"), None, Time(8, 0)), 5)
        train.append_stop(Stop(self.network.get_station("Plovdiv"), Time(9, 0), Time(9, 5)), 5)
        train.append_stop(Stop(self.network.get_station("Burgas"), Time(11, 30), None), 5)
        self.assertEqual(len(train.stops), 3)

    def test_append_stop_rejects_invalid_same_stop_times(self):
        train = PassengerTrain("BV-1235", "Invalid", [], [])
        train.append_stop(Stop(self.network.get_station("Sofia"), None, Time(8, 0)), 5)
        with self.assertRaises(ValueError):
            train.append_stop(Stop(self.network.get_station("Plovdiv"), Time(9, 10), Time(9, 0)), 5)

    def test_validate_schedule_requires_track(self):
        disconnected = RailNetwork()
        disconnected.create_station("A")
        disconnected.create_station("B")
        train = PassengerTrain(
            "BV-1236",
            "NoTrack",
            [],
            [
                Stop(disconnected.get_station("A"), None, Time(8, 0)),
                Stop(disconnected.get_station("B"), Time(9, 0), None),
            ],
        )
        with self.assertRaises(ValueError):
            validate_train_schedule(train, disconnected)

    def test_validate_schedule_rejects_impossible_duration(self):
        train = PassengerTrain(
            "BV-1237",
            "TooFast",
            [],
            [
                Stop(self.network.get_station("Sofia"), None, Time(8, 0)),
                Stop(self.network.get_station("Plovdiv"), Time(8, 30), None),
            ],
        )
        with self.assertRaises(ValueError):
            validate_train_schedule(train, self.network)

    def test_intercity_express_reservation_guards(self):
        train = IntercityExpressTrain(
            "BV-8888",
            "Express",
            [Carriage(CarriageType.BISTRO, 10)],
            [],
        )
        train.reserve_seats(3)
        self.assertEqual(train.reserved_seats, 3)
        self.assertEqual(train.available_seats, 7)

        with self.assertRaises(ValueError):
            train.reserve_seats(0)
        with self.assertRaises(ValueError):
            train.reserve_seats(100)


if __name__ == "__main__":
    unittest.main()
