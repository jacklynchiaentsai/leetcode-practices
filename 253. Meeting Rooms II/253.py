from functools import cmp_to_key
import heapq
"""
custom sorting with minHeap
time: O(nlogn)
space: O(n)
"""
class Solution:
    def compare(self, interval1, interval2):
        if interval1[0] < interval2[0]:
            return -1
        elif interval1[0] == interval2[0]:
            if interval1[1] <= interval2[1]:
                return -1
            else:
                return 1
        else:
            return 1

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=cmp_to_key(self.compare))
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
sort
prioritize room that has earlier end time -> minHeap

"""      
