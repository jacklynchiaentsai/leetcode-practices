"""
greedy
- just want the largest difference between two different arrays
- keep track of min and max number seen so far so can measure gap with every new arrray seen
n = len(arrays)
time: O(n)
space: O(1)
"""
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        # initialize
        # keeps track of current smallest and largest number seen
        curMin = arrays[0][0]
        curMax = arrays[0][len(arrays[0]) - 1]
        curDiff = 0

        for array in arrays[1:]:
            arr_min = array[0]
            arr_max = array[len(array) - 1]

            curDiff = max(curMax-arr_min, arr_max- curMin, curDiff)
            
            curMin = min(curMin, arr_min)
            curMax = max(curMax, arr_max)

        return curDiff
            



            

        
            
