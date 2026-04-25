import csv
import json


def ex01():
    with open("ex01.csv", "w") as f:
        csv_writer = csv.writer(f, delimiter=";")
        csv_writer.writerow(["number", "studentname", "course", "grade"])
        for i in range(1, 11):
            csv_writer.writerow([i, f"Student {i}", "COS 3040", 80 + i])


def ex03():
    try:
        with open("ex01.csv", "r") as f:
            csv_reader = csv.reader(f, delimiter=";")

            print(next(csv_reader))
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print("File not found.")
    except StopIteration:
        print("Empty file.")


def ex0456():
    json_data = '{\
        "id": 123,\
        "studentName": "Ivan Georgiev",\
        "course": "Programming in Python",\
        "grade": 95.0\
    }'

    json_dict = json.loads(json_data)
    print(json_dict)

    for key, value in json_dict.items():
        print(f"{key}: {value}")


def ex08():
    courses = {}

    try:
        with open("ex01.csv", "r") as f:
            csv_reader = csv.DictReader(f, delimiter=";")

            next(csv_reader)
            for row in csv_reader:
                if row["course"] not in courses:
                    courses[row["course"]] = {
                        "members": [],
                        "scores": [],
                        "avgScore": 0
                    }
                try:
                    courses[row["course"]]["members"].append(row["studentname"])
                    courses[row["course"]]["scores"].append(float(row["grade"]))
                    courses[row["course"]]["avgScore"] = sum(
                        courses[row["course"]]["scores"]) / len(courses[row["course"]]["scores"])
                except ValueError:
                    print(f"Invalid grade for {row['studentname']}. Skipping...")
                    
    except FileNotFoundError:
        print("File not found.")
    except StopIteration:
        print("Empty file.")

    print(json.dumps(courses, indent=4))


def ex07():
    courses = {}

    try:
        with open("ex01.csv", "r") as f:
            csv_reader = csv.reader(f, delimiter=";")

            next(csv_reader)
            for row in csv_reader:
                if row[2] not in courses:
                    courses[row[2]] = []
                courses[row[2]].append(row[1])
    except FileNotFoundError:
        print("File not found.")
    except StopIteration:
        print("Empty file.")

    print(json.dumps(courses, indent=4))


if __name__ == "__main__":
    # ex01()
    # ex03()
    # ex0456()
    ex08()
