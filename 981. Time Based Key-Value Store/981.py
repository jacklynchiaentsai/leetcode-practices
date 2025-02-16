"""
binary search
n = len(data_map[key])
m = number of set function calls
time:
    set: O(1)
    get: O(log(n))
space: O(m)
"""
class TimeMap:

    def __init__(self):
        self.data_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data_map:
            self.data_map[key] = []
        
        self.data_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data_map:
            return ""
        
        # check the min timestamp value in key to see if it is <= timestamp
        if self.data_map[key][0][0] > timestamp:
            return ""

        res = ""
        curtime = None
        left = 0
        right = len(self.data_map[key]) - 1

        # want to update res even when left == right
        while left <= right:
            mid = left + (right - left) // 2
            midtime = self.data_map[key][mid][0]

            if midtime > timestamp:
                right = mid - 1
            else:
                # closest we've seen so far to the timestamp
                res = self.data_map[key][mid][1]
                left = mid + 1 # because all times <= timestamp
                
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
"""
intuition brute force linear search so we want to optimize with log(n)

init:
    data_map = {key: [(timestamp, value)]}

set:
    update data_map

get:
    if the key not in data_map:
        return ""
    
    for time from timestamp to 1 -> brute force linear search

    mintime = data_map[key][0][0]
    maxtime = data_map[key][-1][0]

    left = 0
    right = len(data_map[key]) - 1

    while left < right:
        mid
        if data_map[mid] > timestamp:
            right = mid -1
            continue
        
        compare fistnum = abs(timestamp - data_map[mid]), 2ndnum = abs(timestamp - data_map[mid -1])
        if fistnum < 2ndnum:
            left = mid
        else:
            right = mid - 1

        return data_map at key at timestamp right



"""
