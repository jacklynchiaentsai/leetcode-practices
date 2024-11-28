"""
kadane dp + prefix sum
time: O(n)
space: O(n)
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        # solving for normal sum
        curSum = nums[0]
        bestSum = nums[0]

        for i in range(1, n):
            curSum = max(nums[i], curSum + nums[i])
            bestSum = max(curSum, bestSum)

        # solving for special sum
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        prefix_sum[0] = nums[0]
        suffix_sum[n-1] = nums[n-1]

        cumsum = nums[0]
        for i in range(1, n):
            cumsum += nums[i]
            prefix_sum[i] = max(prefix_sum[i-1], cumsum)
        
        cumsum = nums[n-1]
        for i in range(n-2, -1,-1):
            cumsum += nums[i]
            suffix_sum[i] = max(suffix_sum[i+1], cumsum)

        print(prefix_sum)
        print(suffix_sum)
        # enumerate across prefix and suffix sum combinations
        for i in range(0, n-1):
            special_sum = prefix_sum[i] + suffix_sum[i+1] 
            bestSum = max(bestSum, special_sum)

        return bestSum

"""
maximum sum circular subarray
maximum sum can either be
- normal sum from Kadane's maximum subarray problem with no wrap around
- special sum: non overlapping max_prefix_sum + max_suffix sum 
-> create lists for each to enumerate over all possibilities

prefix_sum = [] * len(nums)
prefix_sum[0] = nums[0] # must include first element
current_sum = nums[0]

prefix_sum[i] = max(prefix_sum[i-1], current_sum + prefix_sum[i])
-> need to update current_sum to be cumulative sum

suffix_sum same but backwards
"""
