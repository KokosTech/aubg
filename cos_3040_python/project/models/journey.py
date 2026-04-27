"""Defines journey data used for train route search results."""

from dataclasses import dataclass

from utils.time import Time


@dataclass
class Journey:
    legs: list
    boarding_stops: list
    alighting_stops: list

    @property
    def total_duration(self) -> int:
        """Total duration.
        Parameters:
            None
        Returns:
            int: Return value.
        """
        first_dep = self.boarding_stops[0].departure_time
        last_arr = self.alighting_stops[-1].arrival_time
        return Time.time_diff_minutes(first_dep, last_arr)

    @property
    def departure_time(self) -> Time:
        """Departure time.
        Parameters:
            None
        Returns:
            Time: Return value.
        """
        return self.boarding_stops[0].departure_time

    @property
    def arrival_time(self) -> Time:
        """Arrival time.
        Parameters:
            None
        Returns:
            Time: Return value.
        """
        return self.alighting_stops[-1].arrival_time

    @property
    def num_transfers(self) -> int:
        """Num transfers.
        Parameters:
            None
        Returns:
            int: Return value.
        """
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
                f"\tLeg {i + 1}: {leg.name} ({leg.train_id}) | "
                f"{board.station.name} {board.departure_time.__str__()} → "
                f"{alight.station.name} {alight.arrival_time.__str__()}"
            )
            # show transfer time (layover)
            if i < len(self.boarding_stops) - 1:
                next_board = self.boarding_stops[i + 1]
                transfer_time = Time.time_diff_minutes(alight.arrival_time, next_board.departure_time)
                lines.append(f"\t\tTransfer time: {Time.minutes_to_str(transfer_time)}")

        lines.append("=" * 72)
        return "\n".join(lines)
