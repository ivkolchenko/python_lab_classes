from datetime import datetime, timedelta

class UndergroundSystemError(Exception):
    pass

class UndergroundSystem:
    def __init__(self) -> None:
        self.trips = {}
        self.stations_average = {}

    def check_in(self, passenger_id: str, station: str, time: str) -> None:
        if passenger_id in self.trips:
            raise UndergroundSystemError("Пассажир уже в поездке")

        else:
            self.trips[passenger_id] = (station, datetime.fromisoformat(time))

    def check_out(self, passenger_id: str, station: str, time: str) -> None:
        time_iso = datetime.fromisoformat(time)

        if passenger_id not in self.trips:
            raise UndergroundSystemError("Пассажир еще не начинал поездку")

        else:
            key = (self.trips[passenger_id][0], station)

            if key in self.stations_average:
                count_stations = self.stations_average[key][1]
                self.stations_average[key][0] *= count_stations/(count_stations + 1)
                self.stations_average[key][0] += (
                        (time_iso - self.trips[passenger_id][1])/(count_stations + 1))
                self.stations_average[key][1] += 1

            else:
                self.stations_average[key] = [time_iso - self.trips[passenger_id][1], 1]

            del self.trips[passenger_id]

    def get_average_time(self, start_station, end_station) -> float | None:
        key = (start_station, end_station)

        if key in self.stations_average:
            return self.stations_average[key][0]

        else:
            return None


#Проверка
system = UndergroundSystem()
system.check_in("1", "Sokol", "2026-11-07T14:50")
system.check_in("2", "Sokol", "2026-11-07T14:55")
system.check_out("1", "Kolomenskaya", "2026-11-07T15:20")
assert system.get_average_time("Sokol", "Kolomenskaya") == timedelta(minutes=30)
system.check_out("2", "Kolomenskaya", "2026-11-07T15:35")
assert system.get_average_time("Sokol", "Kolomenskaya") == timedelta(minutes=35)
assert system.get_average_time("Kolomenskaya", "Sokol") is None