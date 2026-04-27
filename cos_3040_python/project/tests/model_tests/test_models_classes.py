import io
import unittest
from contextlib import redirect_stdout

from errors.custom_exceptions import NotFoundError
from models.journey import Journey
from models.rail.track import Track
from models.rail.train_station import TrainStation
from models.trains.helper.carriage import Carriage
from models.trains.helper.carriage_types import CarriageType
from models.trains.helper.stop import Stop
from models.trains.intercity import IntercityTrain
from models.trains.intercity_express import IntercityExpressTrain
from models.trains.passenger import PassengerTrain
from utils.time import Time


class TestModelsClasses(unittest.TestCase):
    def setUp(self):
        self.sofia = TrainStation("Sofia")
        self.plovdiv = TrainStation("Plovdiv")
        self.burgas = TrainStation("Burgas")

    def test_train_station_name_setter_and_str(self):
        station = TrainStation("Stara Zagora")

        # tests setter
        station.name = "Nova Zagora"
        self.assertEqual(str(station), "Nova Zagora")

        # tests for invalid name (regex)
        with self.assertRaises(ValueError):
            station.name = "Sofia-1"

        # tests for empty name
        with self.assertRaises(ValueError):
            station.name = ""

    def test_track_str(self):
        track = Track("Sofia", "Plovdiv", 150.0, 120)
        self.assertEqual("Sofia → Plovdiv | 150.0 km @ max 120 km/h", str(track))

    def test_carriage_setter_and_str(self):
        carriage = Carriage(CarriageType.CLASS1, 30)
        self.assertEqual(carriage.capacity, 30)
        carriage.capacity = 35
        self.assertEqual(carriage.capacity, 35)
        self.assertIn("35 seats", str(carriage))

    def test_carriage_type_enum_values(self):
        expected = {"sleeper", "2nd class", "1st class", "bistro", "quiet", "bike"}
        self.assertEqual({t.value for t in CarriageType}, expected)

    def test_stop_helpers_and_str(self):
        stop1 = Stop(self.sofia, None, Time(8, 0))
        stop2 = Stop(self.plovdiv, Time(9, 0), Time(9, 5))
        stop3 = Stop(self.burgas, Time(7, 55), None)

        # checks for invalid stop timings
        self.assertTrue(Stop.check_validity(stop2))
        self.assertFalse(Stop.check_validity(stop1))

        # checks for incompatible stops (aka out of schedule)
        self.assertTrue(Stop.check_compatibility(stop1, stop2))
        self.assertFalse(Stop.check_compatibility(stop1, stop3))

        # checks for str representation
        self.assertIn("Plovdiv", str(stop2))

    def test_passenger_train_journey_info_add_carriage_and_str(self):
        train = PassengerTrain("BV-4000", "Passenger", [], [])

        # tests journey info
        self.assertIn("no stops scheduled", train.get_journey_info())

        # tests for invalid carriage type
        with self.assertRaises(TypeError):
            train.add_carriage("not a carriage")

        # tests for incompatible carriage type
        with self.assertRaises(ValueError):
            train.add_carriage(Carriage(CarriageType.CLASS1, 20))

        train.add_carriage(Carriage(CarriageType.QUIET, 20))

        # tests for capacity and adding carriage
        self.assertEqual(train.capacity, 20)

        # tests for str representation
        self.assertIn("[Passenger]", str(train))

    def test_base_train_common_methods(self):
        train = PassengerTrain(
            "BV-5000",
            "Base Behavior",
            [Carriage(CarriageType.CLASS2, 40)],
            [
                Stop(self.sofia, None, Time(8, 0)),
                Stop(self.plovdiv, Time(9, 0), Time(9, 3)),
                Stop(self.burgas, Time(11, 20), None),
            ],
        )

        # tests for minute calculation (partial)
        self.assertEqual(train.get_time_length_from_to("Sofia", "Plovdiv"), 60)

        # tests for minute calculation
        self.assertEqual(train.get_time_length_from_to("Sofia", "Burgas"), 200)

        # and for coherence
        self.assertEqual(train.duration, 200)
        self.assertEqual(str(train), "[Passenger] Base Behavior (BV-5000)")

        same_route_later = PassengerTrain(
            "BV-5001",
            "Later Train",
            [],
            [Stop(self.sofia, None, Time(9, 0)), Stop(self.plovdiv, Time(10, 0), None)],
        )

        # tests for comparison - compares departure time
        self.assertTrue(train < same_route_later)  # 08:00 < 09:00
        self.assertTrue(same_route_later > train)  # 09:00 > 08:00

        # tests for removing non-existing carriage
        with self.assertRaises(NotFoundError):
            train.remove_carriage(Carriage(CarriageType.BIKE, 10))

        # tests for removing carriage
        carriage = train.carriages[0]
        train.remove_carriage(carriage)
        self.assertEqual(train.capacity, 0)

    def test_display_helpers_print_output(self):
        train = PassengerTrain("BV-6000", "Display", [], [])
        with io.StringIO() as buf, redirect_stdout(buf):
            train.display_carriages()
            output = buf.getvalue()
        self.assertIn("No carriages", output)

        train.append_stop(Stop(self.sofia, None, Time(8, 0)), 1)
        train.append_stop(Stop(self.plovdiv, Time(9, 0), None), 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            train.display_stops()
            output = buf.getvalue()
        self.assertIn("Stops on", output)
        self.assertIn("Plovdiv", output)
        self.assertIn("Sofia", output)

    def test_intercity_train_specifics(self):
        intercity = IntercityTrain("BV-7000", "Intercity", [], [])
        intercity.add_carriage(Carriage(CarriageType.BISTRO, 30))
        intercity.add_carriage(Carriage(CarriageType.SLEEPER, 20))

        # tests for properties
        self.assertTrue(intercity.has_bistro)

        # tests for serve_food (not implemented yet)
        with self.assertRaises(NotImplementedError):
            intercity.serve_food()

        # tests for str representation
        self.assertIn("[Intercity]", str(intercity))

    def test_intercity_express_requires_bistro_and_str(self):
        # tests for bistro requirement
        with self.assertRaises(ValueError):
            IntercityExpressTrain(
                "BV-8000",
                "No Bistro",
                [Carriage(CarriageType.CLASS1, 20)],
                [],
            )

        express = IntercityExpressTrain(
            "BV-8001",
            "With Bistro",
            [Carriage(CarriageType.BISTRO, 25)],
            [],
        )

        # tests for str representation
        self.assertIn("[Intercity Express]", str(express))

    def test_journey_properties_and_str(self):
        leg1 = PassengerTrain(
            "BV-9000",
            "Leg 1",
            [],
            [Stop(self.sofia, None, Time(8, 0)), Stop(self.plovdiv, Time(9, 0), Time(9, 10))],
        )
        leg2 = PassengerTrain(
            "BV-9001",
            "Leg 2",
            [],
            [Stop(self.plovdiv, None, Time(9, 20)), Stop(self.burgas, Time(11, 0), None)],
        )
        journey = Journey(
            legs=[leg1, leg2],
            boarding_stops=[leg1.stops[0], leg2.stops[0]],
            alighting_stops=[leg1.stops[1], leg2.stops[1]],
        )

        # tests for properties
        self.assertEqual(journey.total_duration, 180)
        self.assertEqual(journey.departure_time, Time(8, 0))
        self.assertEqual(journey.arrival_time, Time(11, 0))
        self.assertEqual(journey.num_transfers, 1)

        # tests for str representation
        self.assertIn("Journey | Sofia", str(journey))

    def test_base_train_comparison_with_non_train(self):
        train = PassengerTrain("BV-9994", "Compare", [], [])
        with self.assertRaises(TypeError):
            _ = train < object()
        with self.assertRaises(TypeError):
            _ = train > object()

if __name__ == "__main__":
    unittest.main()
