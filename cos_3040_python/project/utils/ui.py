import os
import subprocess

from utils.time import Time


def display_menu():
    print("=== TrainSimPy ===")
    print("1. Load data from files")
    print("2. Add...")
    print("3. Modify...")
    print("4. List...")
    print("5. Find a journey")
    print("6. Exit")


# Utility Display Functions

def clear_screen():
    # fun fact, os.system is soft-deprecated (idk since when), but they got subprocess
    subprocess.call("cls" if os.name == "nt" else "clear", shell=True)


def pause():
    input("\nPress Enter to continue...")


# Utility Parse Functions

def parse_time(time_str: str) -> Time | None:
    stripped = time_str.strip()

    if not stripped:
        return None

    try:
        h, m = stripped.split(":")
        return Time(int(h), int(m))
    except ValueError:
        print("Invalid time format. Use HH:MM.")
        return None


def pick_from_list(label: str, options: list[str]) -> str | None:
    if not options:
        print(f"No {label}s available.")
        return None

    print(f"\nSelect a {label}:")

    for i, opt in enumerate(options, 1):
        print(f"\t{i}. {opt}")
    print("\t0. Cancel")

    while True:
        choice = input("Choice: ").strip()

        if choice == "0":
            return None

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

        print("Invalid choice.")
