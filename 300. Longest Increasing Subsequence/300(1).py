"""
intelligently build increasing subsequence + binary search
time: O(n^2)
space: O(n)
"""
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0

        increasing_sub = []

        for num in nums:
            index = bisect.bisect_left(increasing_sub, num)

            # num is greater than all other elements in increasing_sub -> can include to build increasing_sub
            if index == len(increasing_sub):
                increasing_sub.append(num)
            else:
                increasing_sub[index] = num

        return len(increasing_sub)



"""
attempting to construct longest strictly increasing subsequence
motivation: 
- binary search has O(logn) optimize time complexity
- estrictly increasing subsequence is sorted

why increasing_sub[index] = num:
initial thought: only update when index == len(sub) - 1
can replace last element with smaller value while mainaining correct relative order
-> however think about this case: [3,5,6,2,5,4,19,5,6,7,12]
there might be future smaller starting potins that would lead to longer strictly increasing subsequence
-> update increasing_sub and once Im able to create a longer strictly increasing subsequence from it it will start to affect len(sub)

note that increasing_sub may not be the correct answer
"""
