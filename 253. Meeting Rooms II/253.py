from functools import cmp_to_key
import heapq
"""
sorting with minHeap
time: O(nlogn)
space: O(n)
"""
class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = [0]
        heapq.heapify(minHeap)

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if minHeap[0] > start:
                heapq.heappush(minHeap, end)
            else:
                cur_end = heapq.heappop(minHeap)
                heapq.heappush(minHeap, end)

        return len(minHeap)

"""
sorting to process time intervals sequentially; start -> end
preserve a minHeap that gives me the room that is earliest available
minHeap = [earliest available times for each room]
-> initialize minHeap = [0]
for interval in intervals
    if start > minHeap[0]: # can use room
        minHeap.pop()
        minHeap.push(end) # update room available time
    else: # need to create a new room
        minHeap,push(end)

return len(minHeap)
"""      
