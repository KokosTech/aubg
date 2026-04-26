import unittest

from utils.time import Time


class TestTime(unittest.TestCase):
    def test_time_init_normalizes_minute_overflow(self):
        value = Time(10, 125)
        self.assertEqual((value.hour, value.minute), (12, 5))

    def test_time_add_returns_new_time(self):
        start = Time(8, 45)
        end = start + 30
        self.assertEqual(str(end), "09:15")
        self.assertEqual(str(start), "08:45")

    def test_time_diff_wraps_across_midnight(self):
        self.assertEqual(Time.time_diff_minutes(Time(23, 50), Time(0, 10)), 20)

    def test_minutes_to_time_rejects_negative(self):
        with self.assertRaises(ValueError):
            Time.minutes_to_time(-1)

    def test_comparisons_and_equality(self):
        self.assertTrue(Time(9, 0) < Time(10, 0))
        self.assertTrue(Time(10, 0) <= Time(10, 0))
        self.assertTrue(Time(11, 0) > Time(10, 0))
        self.assertTrue(Time(11, 0) >= Time(11, 0))
        self.assertEqual(Time(7, 30), Time(7, 30))


if __name__ == "__main__":
    unittest.main()
