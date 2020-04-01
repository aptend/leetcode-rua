
class UndergroundSystem:

    def __init__(self):
        self.open_trip = {}
        self.complete_trip = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.open_trip[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, st = self.open_trip.pop(id)
        trip = (station, stationName)
        if trip in self.complete_trip:
            self.complete_trip[trip][0] += t - st
            self.complete_trip[trip][1] += 1
        else:
            self.complete_trip[trip] = [t-st, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t, n = self.complete_trip[(startStation, endStation)]
        return t / n




def main():
    undergroundsystem = UndergroundSystem()
    operations = ['checkIn', 'checkIn', 'checkIn', 'checkOut', 'checkOut', 'checkOut', 'getAverageTime', 'getAverageTime', 'checkIn', 'getAverageTime', 'checkOut', 'getAverageTime']
    oprands = [[45, 'Leyton', 3], [32, 'Paradise', 8], [27, 'Leyton', 10], [45, 'Waterloo', 15], [27, 'Waterloo', 20], [32, 'Cambridge', 22], ['Paradise', 'Cambridge'], ['Leyton', 'Waterloo'], [10, 'Leyton', 24], ['Leyton', 'Waterloo'], [10, 'Waterloo', 38], ['Leyton', 'Waterloo']]
    for opt, opd in zip(operations, oprands):
        if hasattr(undergroundsystem, opt):
            print(getattr(undergroundsystem, opt).__call__(*opd))


if __name__ == '__main__':
    main()
