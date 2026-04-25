import configparser
import os

RAILWAYS_FILE = "railways.json"
TRAINS_FILE = "trains.json"
MIN_TRANSFER_TIME = 5
DEFAULT_CARRIAGE_CAPACITY = 60

if os.path.exists("config.ini") and os.path.isfile("config.ini"):
    config = configparser.ConfigParser()

    try:
        with open("config.ini", "r") as f:
            config.read_file(f)
    except FileNotFoundError, IOError:
        print("Error: Problem reading config.ini file.")
        exit(1)
        
    RAILWAYS_FILE = config.get("paths", "railways_file", fallback=RAILWAYS_FILE)
    TRAINS_FILE = config.get("paths", "trains_file", fallback=TRAINS_FILE)
    MIN_TRANSFER_TIME = config.getint("train", "min_transfer_time", fallback=MIN_TRANSFER_TIME)
    DEFAULT_CARRIAGE_CAPACITY = config.getint("train", "default_carriage_capacity", fallback=DEFAULT_CARRIAGE_CAPACITY)
