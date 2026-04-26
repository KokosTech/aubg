from models.trains.helper.time import Time

def time_to_str(time: Time | tuple[int, int] | None):
    if isinstance(time, tuple):
        return f"{time[0]:02d}:{time[1]:02d}" if time else "N/A"

    return time.__str__() if time else "N/A"

def minutes_to_str(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return time_to_str((hours, mins))