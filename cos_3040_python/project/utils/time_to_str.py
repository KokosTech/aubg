def time_to_str(time_tuple):
    return f"{time_tuple[0]:02d}:{time_tuple[1]:02d}" if time_tuple else "N/A"

def minutes_to_str(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return time_to_str((hours, mins))