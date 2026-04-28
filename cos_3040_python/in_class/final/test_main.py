from unittest import TestCase, main

from main import Student


class TestStudent(TestCase):
    def setUp(self):
        self.example_student = Student("John", 25, "123456789")

    def test_student_age(self):
        self.assertEqual(self.example_student.age, 25)
        self.example_student.age = 30
        self.assertEqual(self.example_student.age, 30)

    def test_student_age_invalid(self):
        with self.assertRaises(ValueError):
            self.example_student.age = -10

        with self.assertRaises(ValueError):
            self.example_student.age = 101

        with self.assertRaises(TypeError):
            self.example_student.age = "invalid"

    def test_iadd(self):
        self.example_student += 80
        self.assertEqual(self.example_student.average_grade, 80)
        self.example_student += 50
        self.assertEqual(self.example_student.average_grade, 65)

    def test_iadd_invalid(self):
        with self.assertRaises(TypeError):
            self.example_student += "invalid"
        with self.assertRaises(ValueError):
            self.example_student += -10
        with self.assertRaises(ValueError):
            self.example_student += 101

if __name__ == '__main__':
    main()
