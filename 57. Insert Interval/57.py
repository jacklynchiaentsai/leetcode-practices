"""
overlapping intervals
time: O(n)
space: O(1)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer_list = []
        i = 0

        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            answer_list.append(intervals[i])
            i += 1

        start = newInterval[0]
        end = newInterval[1]

        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        answer_list.append([start,end])

        while i < len(intervals):
            answer_list.append(intervals[i])
            i += 1

        return answer_list
"""
given that original intervals list is sorted and non-overlapping

scenarios for each interval in intervals:
1. non-overlapping with newinterval
- too far ahead to overlap: checking if the start point of newInterval is greater than endPoint of current interval
- too far after to overlap 
2. overlapping with newinterval
thought process: when do intervals start not overlapping with merged intervals
- to check if overlapping we check if the interval's start point <= merged end point

end >= intervals[i][0]
3,8
"""
