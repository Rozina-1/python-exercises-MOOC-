import math
def get_station_data(filename: str):
    station = {}
    from pathlib import Path
    script_dir = Path(__file__).parent
    file_path = script_dir / filename
    with open(file_path) as new_files:
        for line in new_files:
            line = line.strip("\n").split(";")
            if line[0] == "Longitude":
                continue
            name = line[3]
            longitude = float(line[0])
            latitude = float(line[1])
            station[name] = (longitude,latitude)
    return station

def distance(stations: dict, station1: str, station2: str):
    coord = stations[station1]
    longitude1 = coord[0]
    latitude1 = coord[1]
    coord = stations[station2]
    longitude2 = coord[0]
    latitude2 = coord[1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
