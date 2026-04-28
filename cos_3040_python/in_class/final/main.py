from abc import ABC, abstractmethod
from csv import DictReader


class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @name.setter
    def name(self, name: str):
        if len(name.strip()) == 0:
            raise ValueError("Name cannot be empty")
        self._name = name

    @age.setter
    def age(self, age: int):
        if age < 0 or age > 100:
            raise ValueError("Age must be between 0 and 100")
        self._age = age

    @abstractmethod
    def get_details(self):
        pass


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id: str = student_id
        self._grades: list[float] = []

    @property
    def student_id(self) -> str:
        return self._student_id

    @property
    def grades(self) -> list[float]:
        return self._grades

    @property
    def average_grade(self) -> float:
        if not self.grades:
            return -1

        return sum(self.grades) / len(self.grades)

    def get_details(self):
        print("=" * 32)
        print(f"Student: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Average Grade: {"No grades yet" if self.average_grade == -1 else f'{self.average_grade:.2f}'}")
        print(f"Grades: {self.grades if self.grades else 'No grades yet'}")

    def __iadd__(self, grade: float):
        if not isinstance(grade, (float, int)):
            raise TypeError("Grade must be a number")

        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(grade)

        return self

    def __len__(self):
        return len(self.grades)


if __name__ == "__main__":
    students = dict[str, Student]()

    try:
        with open("data.csv", "r") as file:
            data = DictReader(file, delimiter=";")

            for row in data:
                print(row)
                try:
                    if row["id"] not in students:
                        student = Student(row["name"], int(row["age"]), row["id"])
                        students[row["id"]] = student

                    student = students[row["id"]]
                    student += float(row["grade"])
                except ValueError as e:
                    print(f"error fetching student {row['id']}: {e}")
    except FileNotFoundError, IOError:
        print("Problem reading the file")

    print("=" * 32)

    for student in students.values():
        student.get_details()
