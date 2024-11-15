from functools import cmp_to_key
import heapq
"""
chronological ordering
time: O(nlogn)
space: O(n)
"""
class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times_list = []
        for interval in intervals:
            start, end = interval
            times_list.append((start, 1))
            times_list.append((end, -1))

        times_list.sort()

        max_rooms = 0
        cum_rooms = 0
        for tup in times_list:
            time, update = tup
            cum_rooms += update

            max_rooms = max(max_rooms, cum_rooms)
        
        return max_rooms

"""
minimum number of rooms required = maximum number of overlapping meetings
go through time sequentially and iteratively update number of using rooms
time_update = [(time, 1 if time is start time and -1 if time is end time)]

if start time open one more room I need if end time close the room
if same time prioritize end time first so I can close and reuse the room

"""      
