"""
prefix product
time: O(n)
space: O(n)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)

        cumproduct = 1
        for i in range(1, len(nums)):
            cumproduct *= nums[i-1]
            prefix_product[i] = cumproduct
        
        # print(prefix_product)

        cumproduct = 1
        for i in range(len(nums)-2, -1, -1):
            cumproduct *= nums[i+1]
            suffix_product[i] = cumproduct

        # print(suffix_product)

        answer_list = []

        for i in range(0, len(nums)):
            ansprod = prefix_product[i] * suffix_product[i]
            answer_list.append(ansprod)

        return answer_list

"""
prefix product
prefix_product = [] (prefix_product[i] == the prefix product all the way up to i but not including i
suffix_product = [0] * len(nums) (suffix_product[i] == the suffix product all the way up to i but not including i

cumproduct = 1
for i from 1 to len(nums) - 1:
        cumproduct *= nums[i-1]
        append cumproduct to prefix_product


cumproduct = 1
for i from len(nums) - 2 to 0:
    cumproduct *= nums[i+1]
    suffix_product[i] = cumproduct

for i from 0 to len(nums) - 1:
    result_list.append(prefix_product[i] * suffix_product[i])
"""
