"""
two pointer
n = len(height)
time: O(n)
space: O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left_ptr, right_ptr = 0, len(height) - 1
        left_max, right_max = height[left_ptr], height[right_ptr]

        cum_water = 0
        while left_ptr < right_ptr:
            if left_max <= right_max:
                left_ptr += 1
                cum_val = left_max - height[left_ptr]
                if cum_val > 0:
                    cum_water += cum_val
                
                left_max = max(left_max, height[left_ptr])
            
            else:
                right_ptr -= 1
                cum_val = right_max - height[right_ptr]
                if cum_val > 0:
                    cum_water += cum_val
                
                right_max = max(right_max, height[right_ptr])
        
        return cum_water
"""
min(left max height, right max height) - h[i]
<=0 -> 0
>0 -> trap water

to conserve memory space we can update left_max and right_max as we go

to update left_max and right_max we need a left_pointer that starts from the very beginning of height and a right_pointer that starts from the very end of height

left_ptr = 0 
right_ptr = len(height) - 1

left_max = height at left_ptr
right_max = height at right_ptr

cum_water = 0

while left_p[tr < right_ptr:
    at each iteration want to update the pointer with the smaller max value
    we want to see if we can find a larger max height

    if height at left_ptr <= height at right_ptr:
        update left_ptr by 1
        calculate cum_water at position left_ptr
            cum_water += min(left_max, right_max) - height[left_ptr]
        left_max = max(left_max, height at left_ptr)
        

    else:
        do the same as above but for right pointer

note: we already know at each end that we can't possibly trap any water
"""
