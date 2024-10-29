import bisect
"""
binary search
time: O(nlogn)
space: O(n)
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sequences = [nums.pop()]

        for num in nums[::-1]:
            idx = bisect.bisect(sequences, num)

            if idx == len(sequences):
                sequences.append(num)
            else:
                sequences[idx] = num

        return len(sequences)


"""
intuition:
O(n^2) solution: for each operation iterate through the list to try find longest increasing subsequence -> mark as visited until all are visited


APPROACH FOR STRICTLY DECREASING SUBSEQUENCE:
single iteration:
we use a list sequences to keep track of the last element of each subseqeunce
-> each element in list will be a subsequence

everytime encounter new value in nums, use binary search to find appropriate position of num in sequences
- if larger than all values in sequences bisect_right ==len(sequences)
-> start new sequence append to sequences
- otherwise update the sequence at the current position
* THIS WORKS FOR STRICTLY DECREASING BECAUSE FOR LIST YOU CAN APPEND TO RIGHT IN O(1) BUT CANNOT PREPEND IN O(1) making direct adaptation to strictly increasing very costly

ADJUSTMENT:
treat it as strictly decreasing problem by reversing the nums array
-> strictly increasing == <- strictly decreasing
"""
