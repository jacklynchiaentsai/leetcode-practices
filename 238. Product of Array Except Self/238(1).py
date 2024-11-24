"""
prefix product
time: O(n)
space: O(1)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer_list = [1] * len(nums)

        cumproduct = 1
        for i in range(1, len(nums)):
            cumproduct *= nums[i-1]
            answer_list[i] = cumproduct
        

        cumproduct = 1
        for i in range(len(nums)-2, -1, -1):
            cumproduct *= nums[i+1]
            answer_list[i] *= cumproduct

        return answer_list

"""
optimizing space complexity by using the output data structure for storage
"""
