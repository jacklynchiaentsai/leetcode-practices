"""
overlapping intervals (sorting)
time: O(nlogn)
space: O(1)
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        return_list = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            curstart = intervals[i][0]
            curend = intervals[i][1]

            if curstart <= end:
                end = max(end, curend)
            else:
                return_list.append([start, end])
                start = curstart
                end = curend

        return_list.append([start, end])

        return return_list

"""
sort intervals by start -> end
curstart
curend

nextstart
nextend

if nextstart <= curend -> overlapping
else -> non-overlapping


sort intervals by start -> end
return_list = []

start = intervals[0][0]
end = intervals[0][1]

iterate i from 1 to len(intervals) - 1:
    curstart, curend

    if curstart <= end -> overlapping{
        end = max(end, curend)
    }
    else -> non-overlapping{
        add [start,end] to return_list
        start, end = curstart, curend
    }

add [start,end] to return_list


"""
