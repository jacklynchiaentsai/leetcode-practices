"""
nested dictionary
time:
- checkIn: O(1)
- checkOut: O(1)
- getAverageTime:O(1)

space: O(m + n^2)
m = num of different customers
n = number of stations
"""
class UndergroundSystem:

    def __init__(self):
        self.checkin_dict = {}
        self.average_dict = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_dict[id] = {"station": stationName, "time":  t}
    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinstation = self.checkin_dict[id]["station"]
        checkintime = self.checkin_dict[id]["time"]

        if checkinstation not in self.average_dict:
            self.average_dict[checkinstation] = {}

        if stationName not in self.average_dict[checkinstation]:
            self.average_dict[checkinstation][stationName] = {"timesum": 0, "numtravel": 0}
        
        self.average_dict[checkinstation][stationName]['timesum'] += t - checkintime
        self.average_dict[checkinstation][stationName]['numtravel'] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        timesum = self.average_dict[startStation][endStation]['timesum']
        numtravel = self.average_dict[startStation][endStation]['numtravel']
        return timesum / numtravel


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

"""
checkin_dict = {id: {checkinstation: , checkintime:}}
average_dict = {startStation: {endStation: {timesum: , numtravel}}}

init:
checkin_dict
average_dict

checkin:
update checkin_dict

checkout:
access checkin_dict[id]
update average_dict
delete checkin_dict[id]

getAverageTime:
query average_dict = timesum / numtravel

"""
