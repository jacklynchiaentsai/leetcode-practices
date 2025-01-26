"""
observation + algorithm dev + memorization
n = len(height)
time: O(n)
space: O(n)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max_list = [0] * len(height)
        right_max_list = [0] * len(height)

        cur_max = 0
        for i, h in enumerate(height):
            left_max_list[i] = cur_max
            cur_max = max(cur_max, h)

        cur_max = 0
        for i in range(len(height) - 1, -1, -1):
            right_max_list[i] = cur_max
            cur_max = max(cur_max, height[i])

        cum_water = 0
        for i, h in enumerate(height):
            cur_val = min(left_max_list[i], right_max_list[i]) - h
            if cur_val > 0:
                cum_water += cur_val
        
        return cum_water
        

"""
min(left max height, right max height) - h[i]
<=0 -> 0
>0 -> trap water

left_max_list 
right_max_list

left_max = 0
for i, h in height:
    left_max_list[i] = left_max
    left_max = max(left_max, h)

cum_water = 0

"""
