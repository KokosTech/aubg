import configparser

config = configparser.ConfigParser()

try:
    with open("config.ini", "r") as f:
        config.read_file(f)
except FileNotFoundError:
    print("Error: config.ini file not found. Please create a config.ini file with the necessary settings.")
    exit(1)

STATIONS_FILE = config["paths"]["stations_file"]
RAILWAYS_FILE = config["paths"]["railways_file"]
TRAINS_FILE = config["paths"]["trains_file"]

DEFAULT_CARRIAGE_CAPACITY = config.getint("train", "default_carriage_capacity")
