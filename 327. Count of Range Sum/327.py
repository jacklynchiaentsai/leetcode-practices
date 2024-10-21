"""
math + sorted list (self balancing BST)
time: O(nlog(n))
space: O(n)
"""
from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixSumList = SortedList([0])
        cursum = 0
        totnum = 0
        for num in nums:
            cursum += num
            totnum += prefixSumList.bisect_right(cursum - lower) - prefixSumList.bisect_left(cursum - upper)
            prefixSumList.add(cursum)

        return totnum
        

"""
mathematical (experience): range sums
define S_j as the sum of elements all the way up to index j
range sum of range [i,j] = S_j - S_{i-1}
lower <= Sij <= upper
lower <= S_j - S_{i-1} <= upper
we know lower, upper and can calculate S_j
we have to find all the S_{i-1} that satisfies
S_j - upper <= S_{i-1} <= S_j - lower

-> we can store prefix sums in a sorted list to enable efficient querying
"""
