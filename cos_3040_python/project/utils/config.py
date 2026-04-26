import configparser
import os

CONFIG_FILE = "config.ini"

RAILWAYS_FILE = "railways.json"
TRAINS_FILE = "trains.json"
MIN_TRANSFER_TIME = 5
DEFAULT_CARRIAGE_CAPACITY = 60

if os.path.exists(CONFIG_FILE) and os.path.isfile(CONFIG_FILE):
    config = configparser.ConfigParser()

    try:
        with open(CONFIG_FILE, "r") as f:
            config.read_file(f)
    except (FileNotFoundError, IOError) as e:
        raise RuntimeError(f"Problem reading {CONFIG_FILE} file: {e}") from e

    RAILWAYS_FILE = config.get("paths", "railways_file", fallback=RAILWAYS_FILE)
    TRAINS_FILE = config.get("paths", "trains_file", fallback=TRAINS_FILE)
    MIN_TRANSFER_TIME = config.getint("train", "min_transfer_time", fallback=MIN_TRANSFER_TIME)
    DEFAULT_CARRIAGE_CAPACITY = config.getint("train", "default_carriage_capacity", fallback=DEFAULT_CARRIAGE_CAPACITY)
