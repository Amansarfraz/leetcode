class UndergroundSystem(object):

    def __init__(self):
        self.checkin = {}
        self.travel = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkin[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, startTime = self.checkin.pop(id)
        route = (startStation, stationName)
        travelTime = t - startTime

        if route not in self.travel:
            self.travel[route] = [0, 0]

        self.travel[route][0] += travelTime
        self.travel[route][1] += 1

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        totalTime, count = self.travel[(startStation, endStation)]
        return float(totalTime) / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id, stationName, t)
# obj.checkOut(id, stationName, t)
# param_3 = obj.getAverageTime(startStation, endStation)