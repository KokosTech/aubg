"""Check that a train's stop times are physically possible given track constraints."""


def validate_train_schedule(train, rail_network):
    stops = train.stops
    for i in range(len(stops) - 1):
        from_id = stops[i].station.name
        to_id = stops[i + 1].station.name

        track = rail_network.get_track(from_id, to_id)

        # Convert times to minutes for calculation
        arrival_time = stops[i + 1].arrival_time
        departure_time = stops[i].departure_time

        if arrival_time and departure_time:
            if track is None:
                raise ValueError(
                    f"Missing track between {from_id} and {to_id} for train schedule validation"
                )
            scheduled_minutes = arrival_time.to_minutes - departure_time.to_minutes
            min_minutes = (track.distance_km / track.max_speed_kmh) * 60

            if scheduled_minutes < min_minutes:
                raise ValueError(
                    f"Schedule impossible between {from_id} and {to_id}: "
                    f"scheduled {scheduled_minutes:.0f} minutes, minimum possible {min_minutes:.0f} minutes"
                )
