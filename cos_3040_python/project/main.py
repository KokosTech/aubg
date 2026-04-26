"""

# Project: COS 3040 Python Project

"""


import os
import subprocess

from models.rail.rail_network import RailNetwork
from models.trains.helper.stop import Stop
from models.trains.intercity import IntercityTrain
from models.trains.intercity_express import IntercityExpressTrain
from models.trains.passenger import PassengerTrain
from services.train_sim import TrainSim
from utils.config import DEFAULT_CARRIAGE_CAPACITY, RAILWAYS_FILE, TRAINS_FILE
from utils.time import Time
from errors.custom_exceptions import NotFoundError
from models.trains.helper.carriage import Carriage
from models.trains.helper.carriage_types import CarriageType

# -------------------------------------------------------------------------
# Globals
# -------------------------------------------------------------------------

network = RailNetwork()
sim = TrainSim(network)


# -------------------------------------------------------------------------
# Utility
# -------------------------------------------------------------------------

def clear_screen():
    subprocess.call("cls" if os.name == "nt" else "clear", shell=True)


def pause():
    input("\nPress Enter to continue...")


def parse_time(time_str: str) -> Time | None:
    if not time_str.strip():
        return None
    try:
        h, m = time_str.strip().split(":")
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
        print(f"  {i}. {opt}")
    print("  0. Cancel")
    while True:
        choice = input("Choice: ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid choice.")


# -------------------------------------------------------------------------
# Load
# -------------------------------------------------------------------------

def handle_load():
    clear_screen()
    print("=== Load Data ===")
    try:
        network.load_from_json(RAILWAYS_FILE)
        print(f"✓ Stations loaded from {RAILWAYS_FILE}")
        sim.load_trains_from_json(TRAINS_FILE)
        print(f"✓ Trains loaded from {TRAINS_FILE}")
    except FileNotFoundError:
        pass  # handled by the classes themselves
    except Exception as e:
        print(f"Error loading data: {e}")
    pause()


# -------------------------------------------------------------------------
# Add submenu
# -------------------------------------------------------------------------

def handle_add():
    while True:
        clear_screen()
        print("=== Add ===")
        print("1. Add station")
        print("2. Add track")
        print("3. Add train")
        print("4. Add stop to train")
        print("5. Add carriage to train")
        print("0. Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_station()
        elif choice == "2":
            add_track()
        elif choice == "3":
            add_train()
        elif choice == "4":
            add_stop()
        elif choice == "5":
            add_carriage_to_train()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def add_station():
    clear_screen()
    print("=== Add Station ===")
    name = input("Station name: ").strip()
    try:
        station = network.create_station(name)
        print(f"✓ Station '{station.name}' added.")
        network.save_to_json(RAILWAYS_FILE)
    except (ValueError, NotFoundError) as e:
        print(f"Error: {e}")
    pause()


def add_track():
    clear_screen()
    print("=== Add Track ===")
    station_names = list(network.stations.keys())
    from_name = pick_from_list("departure station", station_names)
    if not from_name:
        return
    to_name = pick_from_list("destination station", station_names)
    if not to_name:
        return
    try:
        distance = float(input("Distance (km): ").strip())
        max_speed = int(input("Max speed (km/h): ").strip())
        network.create_track(from_name, to_name, distance, max_speed)
        print(f"✓ Track {from_name} → {to_name} added.")
        network.save_to_json(RAILWAYS_FILE)
    except (ValueError, NotFoundError) as e:
        print(f"Error: {e}")
    pause()


def add_train():
    clear_screen()
    print("=== Add Train ===")
    print("Train type:")
    print("  1. Passenger")
    print("  2. Intercity")
    print("  3. Intercity Express")
    type_choice = input("Choice: ").strip()

    train_map = {
        "1": PassengerTrain,
        "2": IntercityTrain,
        "3": IntercityExpressTrain
    }
    train_class = train_map.get(type_choice)
    if not train_class:
        print("Invalid choice.")
        pause()
        return

    try:
        train_id = input("Train ID (e.g. BV-1234): ").strip()
        name = input("Train name: ").strip()
        train = train_class(train_id, name, [], [])
        sim.add_train(train)
        print(f"✓ Train '{name}' ({train_id}) added.")
        sim.save_trains_to_json(TRAINS_FILE)
    except (ValueError, NotFoundError) as e:
        print(f"Error: {e}")
    pause()


def add_stop():
    clear_screen()
    print("=== Add Stop to Train ===")
    train_ids = list(sim.trains.keys())
    train_id = pick_from_list("train", train_ids)
    if not train_id:
        return

    clear_screen()
    station_names = list(network.stations.keys())
    station_name = pick_from_list("station", station_names)
    if not station_name:
        return

    try:
        arrival_str = input(f"Arrival time on {station_name} (HH:MM, leave blank if first stop): ").strip()
        departure_str = input(f"Departure time {station_name} (HH:MM, leave blank if last stop): ").strip()
        arrival = parse_time(arrival_str) if arrival_str else None
        departure = parse_time(departure_str) if departure_str else None

        station = network.get_station(station_name)
        stop = Stop(station=station, arrival_time=arrival, departure_time=departure)
        sim.add_stop_to_train(train_id, stop)
        print(f"✓ Stop at '{station_name}' added to train '{train_id}'.")
        sim.save_trains_to_json(TRAINS_FILE)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    pause()


# -------------------------------------------------------------------------
# Modify submenu
# -------------------------------------------------------------------------

def handle_modify():
    while True:
        clear_screen()
        print("=== Modify ===")
        print("1. Rename station")
        print("2. Remove station")
        print("3. Remove track")
        print("4. Remove train")
        print("5. Remove carriage from train")
        print("0. Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            rename_station()
        elif choice == "2":
            remove_station()
        elif choice == "3":
            remove_track()
        elif choice == "4":
            remove_train()
        elif choice == "5":
            remove_carriage_from_train()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def rename_station():
    clear_screen()
    print("=== Rename Station ===")
    name = pick_from_list("station", list(network.stations.keys()))
    if not name:
        return
    try:
        new_name = input("New name: ").strip()
        network.rename_station(name, new_name)
        print(f"✓ Renamed '{name}' to '{new_name}'.")
        network.save_to_json(RAILWAYS_FILE)
    except (ValueError, NotFoundError) as e:
        print(f"Error: {e}")
    pause()


def remove_station():
    clear_screen()
    print("=== Remove Station ===")
    name = pick_from_list("station", list(network.stations.keys()))
    if not name:
        return
    try:
        # Remove trains using this station
        removed_trains = sim.remove_trains_using_station(name)
        if removed_trains:
            print(f"  Removed trains: {', '.join(removed_trains)}")

        network.remove_station(name)
        print(f"✓ Station '{name}' removed.")
        network.save_to_json(RAILWAYS_FILE)
        sim.save_trains_to_json(TRAINS_FILE)
    except (ValueError, NotFoundError) as e:
        print(f"Error: {e}")
    pause()


def remove_track():
    clear_screen()
    print("=== Remove Track ===")
    track_labels = [
        f"{t.from_station_id} → {t.to_station_id}"
        for t in network.tracks
    ]
    label = pick_from_list("track", track_labels)
    if not label:
        return
    try:
        from_id, to_id = [s.strip() for s in label.split("→")]

        # Remove trains using this track
        removed_trains = sim.remove_trains_using_track(from_id, to_id)
        if removed_trains:
            print(f"  Removed trains: {', '.join(removed_trains)}")

        network.remove_track(from_id, to_id)
        print(f"✓ Track {from_id} → {to_id} removed.")
        network.save_to_json(RAILWAYS_FILE)
        sim.save_trains_to_json(TRAINS_FILE)
    except (ValueError, NotFoundError) as e:
        print(f"Error: {e}")
    pause()


def remove_train():
    clear_screen()
    print("=== Remove Train ===")
    train_id = pick_from_list("train", list(sim.trains.keys()))
    if not train_id:
        return
    try:
        sim.remove_train(train_id)
        print(f"✓ Train '{train_id}' removed.")
        sim.save_trains_to_json(TRAINS_FILE)
    except (ValueError, NotFoundError) as e:
        print(f"Error: {e}")
    pause()


def add_carriage_to_train():
    clear_screen()
    print("=== Add Carriage to Train ===")
    train_ids = list(sim.trains.keys())
    train_id = pick_from_list("train", train_ids)
    if not train_id:
        return

    train = sim.get_train(train_id)

    clear_screen()
    print(f"Train: {train}")
    print("\nCarriage types:")
    carriage_types = [ct.value for ct in CarriageType]
    carriage_type_name = pick_from_list("carriage type", carriage_types)
    if not carriage_type_name:
        return

    try:
        carriage_type = CarriageType(carriage_type_name)
        capacity_str = input(f"Capacity (default {DEFAULT_CARRIAGE_CAPACITY}): ").strip()
        capacity = int(capacity_str) if capacity_str else DEFAULT_CARRIAGE_CAPACITY

        carriage = Carriage(carriage_type, capacity)
        train.add_carriage(carriage)
        print(f"✓ {carriage} added to train '{train_id}'.")
        sim.save_trains_to_json(TRAINS_FILE)
    except (ValueError, TypeError, NotFoundError) as e:
        print(f"Error: {e}")
    pause()


def remove_carriage_from_train():
    clear_screen()
    print("=== Remove Carriage from Train ===")
    train_ids = list(sim.trains.keys())
    train_id = pick_from_list("train", train_ids)
    if not train_id:
        return

    train = sim.get_train(train_id)

    if not train.carriages:
        print("This train has no carriages.")
        pause()
        return

    clear_screen()
    print(f"Train: {train}")
    print("\nCarriages:")
    carriage_labels = [f"{i}. {c}" for i, c in enumerate(train.carriages, 1)]
    carriage_label = pick_from_list("carriage", [c[3:] for c in carriage_labels])
    if not carriage_label:
        return

    try:
        # Find the carriage by its string representation
        carriage_to_remove = None
        for c in train.carriages:
            if str(c) == carriage_label:
                carriage_to_remove = c
                break

        if carriage_to_remove is None:
            print("Error: Carriage not found")
            pause()
            return

        train.remove_carriage(carriage_to_remove)
        print(f"✓ Carriage removed from train '{train_id}'.")
        sim.save_trains_to_json(TRAINS_FILE)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    pause()


# -------------------------------------------------------------------------
# List submenu
# -------------------------------------------------------------------------

def handle_list():
    while True:
        clear_screen()
        print("=== List ===")
        print("1. List stations")
        print("2. List tracks")
        print("3. List trains")
        print("4. Display full network")
        print("0. Back")
        choice = input("Choice: ").strip()

        if choice == "1":
            clear_screen()
            print("=== Stations ===")
            for s in network.stations.values():
                print(f"  - {s}")
            pause()
        elif choice == "2":
            clear_screen()
            print("=== Tracks ===")
            for t in network.tracks:
                print(f"  - {t.from_station_id} → {t.to_station_id} | {t.distance_km} km @ {t.max_speed_kmh} km/h")
            pause()
        elif choice == "3":
            clear_screen()
            print("=== Trains ===")
            for train in sim.trains.values():
                print(f"  - {train}")
                train.display_stops()
            pause()
        elif choice == "4":
            clear_screen()
            network.display_network()
            pause()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


# -------------------------------------------------------------------------
# Search
# -------------------------------------------------------------------------

def handle_search():
    clear_screen()
    print("=== Find Journey ===")

    station_names = list(network.stations.keys())
    from_name = pick_from_list("departure station", station_names)
    if not from_name:
        return
    to_name = pick_from_list("destination station", station_names)
    if not to_name:
        return

    time_str = input("Earliest departure time (HH:MM, leave blank for any): ").strip()
    departure_time = parse_time(time_str) if time_str else None

    direct_input = input("Direct trains only? (y/n): ").strip().lower()
    direct_only = direct_input == "y"

    print("Sort by:")
    print("  1. Departure time (default)")
    print("  2. Duration")
    sort_choice = input("Choice: ").strip()
    sort_by = "duration" if sort_choice == "2" else "departure_time"

    try:
        journeys = sim.search_journeys(
            from_station=from_name,
            to_station=to_name,
            departure_time=departure_time,
            direct_only=direct_only,
            sort_by=sort_by
        )

        clear_screen()
        print(f"=== Journeys: {from_name} → {to_name} ===\n")
        if not journeys:
            print("No journeys found.")
        else:
            for i, journey in enumerate(journeys, 1):
                print(f"{i}. {journey}\n")
    except ValueError as e:
        print(f"Error: {e}")
    pause()


# -------------------------------------------------------------------------
# Main menu
# -------------------------------------------------------------------------

def display_menu():
    print("=== TrainSimPy ===")
    print("1. Load data from files")
    print("2. Add...")
    print("3. Modify...")
    print("4. List...")
    print("5. Find a journey")
    print("6. Exit")


def main():
    while True:
        clear_screen()
        display_menu()
        choice = input("Choice: ").strip()

        clear_screen()
        if choice == "1":
            handle_load()
        elif choice == "2":
            handle_add()
        elif choice == "3":
            handle_modify()
        elif choice == "4":
            handle_list()
        elif choice == "5":
            handle_search()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
