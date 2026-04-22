import configparser

config = configparser.ConfigParser()

try:
    with open("config.ini", "r") as f:
        config.read_file(f)
except FileNotFoundError:
    print("Error: config.ini file not found. Please create a config.ini file with the necessary settings.")
    exit(1)

RAILWAYS_FILE = config["paths"]["railways_file"]
TRAINS_FILE = config["paths"]["trains_file"]
MIN_TRANSFER_TIME = config.getint("train", "min_transfer_time")

DEFAULT_CARRIAGE_CAPACITY = config.getint("train", "default_carriage_capacity")
