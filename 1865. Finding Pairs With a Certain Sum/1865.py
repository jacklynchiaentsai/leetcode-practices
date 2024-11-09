"""
pairsum -> dictionary frequencies
m = len(nums1)
n = len(nums2)
initialization:
time: O(m + n)
space: O(m + n)
add:
- time: O(1)
- space: O(1)
count:
- time: O(min(m,n))
- space: O(1)

"""
import collections
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_freq = Counter(nums1)
        self.nums2_freq = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.nums2[index] += val

        self.nums2_freq[old_val] -= 1
        if self.nums2_freq[old_val] == 0:
            del self.nums2_freq[old_val]
        
        self.nums2_freq[self.nums2[index]] += 1
 
    def count(self, tot: int) -> int:
        # iterate throught the list with the smaller number of unique items
        smaller_dict = None
        larger_dict = None
        if len(self.nums1_freq) <= len(self.nums2_freq):
            smaller_dict = self.nums1_freq
            larger_dict = self.nums2_freq
        else:
            smaller_dict = self.nums2_freq
            larger_dict = self.nums1_freq

        total_count = 0
        for key, value in smaller_dict.items():
            total_count += larger_dict[tot-key] * smaller_dict[key]

        return total_count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

"""
intuition (not fast enough for SIG)
add operation: O(1) time
- update nums2 directly
count operation: O(n)
- num1_freq_dict = {ele: freq}
for ele in nums2
    total_pairs += num1_freq_dict[tot - ele]

faster: want to make add and count both O(1)
initialization
- num1_freq_dict = {ele: freq}
- nums2_freq_dict = {ele: freq}
- pairsum_dict = {sum: freq}

add operation
- old_val = nums2[i]
- 

count operation


"""
