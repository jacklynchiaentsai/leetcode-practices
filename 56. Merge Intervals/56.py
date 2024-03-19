"""
customized sorting
time: O(nlogn)
space: O(n)
"""
from functools import cmp_to_key
class Solution:
    def cmp(self, interval1, interval2):
        if interval1[0] < interval2[0]:
            return -1
        elif interval1[0] > interval2[0]:
            return 1
        else:
            if interval1[1] < interval2[1]:
                return -1
            else:
                return 1

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        sorted_intervals = sorted(intervals, key = cmp_to_key(self.cmp))
        for interval in sorted_intervals:
            if len(output) == 0:
                output.append(interval)
            else:
                prevstart = output[-1][0]
                prevend = output[-1][1]
                start = interval[0]
                end = interval[1]
                if end >= prevend:
                    if start > prevend:
                        output.append(interval)
                    else:
                        output[-1][1] = end
        
        return output
"""
intervals = [[1,3],[2,6],[8,10],[15,18]]
sorting by starting point and then by end point
1)next interval eats previous interval up
2) next interval partially overlapping but having a bit left or completely overlapping
3) non overlapping
[[1,3], [4,5], [4,6], ]

"""
