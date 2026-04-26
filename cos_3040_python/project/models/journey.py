from dataclasses import dataclass
from models.trains.base import BaseTrain
from models.trains.helper.stop import Stop
from utils.time import Time


@dataclass
class Journey:
    legs: list
    boarding_stops: list
    alighting_stops: list

    @property
    def total_duration(self) -> int:
        first_dep = self.boarding_stops[0].departure_time
        last_arr = self.alighting_stops[-1].arrival_time
        return (last_arr[0] * 60 + last_arr[1]) - (first_dep[0] * 60 + first_dep[1])

    @property
    def departure_time(self) -> tuple[int, int]:
        return self.boarding_stops[0].departure_time

    @property
    def num_transfers(self) -> int:
        return len(self.legs) - 1

    def __str__(self):
        lines = [
            f"Journey | {self.boarding_stops[0].station.name} → "
            f"{self.alighting_stops[-1].station.name} | "
            f"Duration: {Time.minutes_to_str(self.total_duration)} | "
            f"Transfers: {self.num_transfers}"
        ]
        for i, (leg, board, alight) in enumerate(
            zip(self.legs, self.boarding_stops, self.alighting_stops)
        ):
            lines.append(
                f"  Leg {i + 1}: {leg.name} ({leg.train_id}) | "
                f"{board.station.name} {board.departure_time.__str__()} → "
                f"{alight.station.name} {alight.arrival_time.__str__()}"
            )
        return "\n".join(lines)
