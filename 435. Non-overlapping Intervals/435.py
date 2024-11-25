"""
sorting + greedy
time: O(nlogn)
space: O(n) -> python sorting algorithm
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]

        minnum = 0
        for i in range(1, len(intervals)):
            curstart, curend = intervals[i]

            if curstart < end:
                if curend <= end:
                    start = curstart
                    end = curend

                minnum += 1

            else:
                start = curstart
                end = curend

        return minnum
"""
greedy: sort by start -> end 
start, end -> existing interval

for interval in intervals:
curstart, curend

if curstart < prevend -> overlapping {
    remove the interval with the larger endpoint -> set start, end accordingly
    minnum += 1
}
else -> not overlapping{
    start, end = curstart, curend
}
"""
