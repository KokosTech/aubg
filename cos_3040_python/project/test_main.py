from services.validate_train_schedule import validate_train_schedule
from models.Carriage import Carriage, CarriageType
from models.Stop import Stop
from models.PassengerTrain import PassengerTrain
from models.TrainStation import TrainStation
from models.RailNetwork import RailNetwork

from utils.config import RAILWAYS_FILE


# --- Network setup ---
network = RailNetwork()
network.create_station("Sofia Central")
network.create_station("Plovdiv Central")
network.create_station("Varna Central")

network.create_track("Sofia Central", "Plovdiv Central", distance_km=150.0, max_speed_kmh=120)
network.create_track("Plovdiv Central", "Varna Central", distance_km=250.0, max_speed_kmh=100)

# print(network)
network.display_network()
network.save_to_json(RAILWAYS_FILE)
# print(network.get_tracks_from("Sofia Central"))

# --- Train setup ---
c1 = Carriage(CarriageType.CLASS1, capacity=30)
c2 = Carriage(CarriageType.QUIET, capacity=40)

s1 = Stop(network.get_station("Sofia Central"), None, (8, 0))
s2 = Stop(network.get_station("Plovdiv Central"), (9, 15), (9, 20))
s3 = Stop(network.get_station("Varna Central"), (11, 55), None)

train = PassengerTrain("BV-1234", "Balkan Express", [c1, c2], [s1, s2, s3])
train.display_carriages()
train.display_stops()

# print(train)
# print(train.get_journey_info())
# print(f"Total capacity: {train.capacity}")

# --- Validate schedule against network ---
validate_train_schedule(train, network)
