"""
3 pointer solution + observation
time: O(m+n)
space: O(1)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = m-1, n-1
        replace_ptr = m+n-1

        while replace_ptr >=0:
            if ptr1 < 0:
                nums1[replace_ptr] = nums2[ptr2]
                ptr2 -= 1
            elif ptr2 < 0 or nums1[ptr1] > nums2[ptr2]:
                nums1[replace_ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                if nums2[ptr2] >= nums1[ptr1]:
                    nums1[replace_ptr] = nums2[ptr2]
                    ptr2 -= 1
                else:
                    nums1[replace_ptr] = nums1[ptr1]
                    ptr1 -= 1

            replace_ptr -= 1
        
"""
m == 0: transfer everything from nums2 to nums1
n == 0: return nums1

initial solution:
ptr1, ptr2
sorted_li = []
while have not exhausted both ptrs:
    add the smaller pointer's value into sorted_li and increment the pointer by 1
    if either one of the pointers are exhausted then we simply add the non-exhausted pointer's value and update the pointer

update nums1 to match the sorted_li

updated solution:
ptr1 = m-1, ptr2 = n-1
replace_ptr = (m+n-1) index in which we're replacing in nums1

while replace_ptr > 0:
    compare ptr1 and ptr2's value replace nums1[replace_ptr] with the larger value and update the ptr accordingly
    if either one of the pointers are exhausted then we simply use the non-exhausted pointer's value and update the pointer
    replace_ptr -= 1
"""
