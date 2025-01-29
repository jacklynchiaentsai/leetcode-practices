"""
binary search
m = len(nums1)
n = len(nums2)
time: O(log(min(m,n)))
space: O(1)
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = nums2, nums1
        
        m = len(A)
        n = len(B)

        if m == 0:
            if n % 2 == 0:
                return (B[n//2] + B[n // 2 - 1]) / 2
            else:
                return B[n//2]

        
        total = m+n
        half = (m+n) // 2
        left = 0
        right = len(A) - 1
        
        while True:
            med = left + (right - left) // 2

            partB = half - (med + 1) - 1

            rightmostleftA = A[med] if med >=0  else float('-inf')
            leftmostrightA = A[med + 1] if (med + 1) <m  else float('inf')
            rightmostleftB = B[partB] if partB >=0 else float('-inf')
            leftmostrightB = B[partB + 1] if (partB + 1) <n else float('inf') 
            # check for out of bounds

            if rightmostleftA <= leftmostrightB and rightmostleftB <= leftmostrightA:
                if total % 2 ==0:
                    rightmostleft = max(rightmostleftA, rightmostleftB)
                    leftmostright = min(leftmostrightA, leftmostrightB)
                    return (rightmostleft + leftmostright) / 2
                else:
                    return min(leftmostrightA, leftmostrightB)
            
            elif rightmostleftA > leftmostrightB:
                right = med - 1
            else:
                left = med + 1


"""
edge: either one of the arrays are empty return median of the non-empty array

ptr1
ptr2
sorted_list 
           p
nums1 =  -inf [1,3,4] + inf, 
nums2 = [1,2,5,6,7]
         l m      r

med = l + (r-l) //2

1 1 2 3 | 4 5 6 
output = 3.5
total = 8
half = 4

total = 7
half = 3

if m+n is odd:
    sorted_list[(m+n)// 2 +1]
    (m+n)// 2 on either side of median
else:
    (m+n) // 2 on left and right
    median = average of rightmost of left and the lefmost right

"""
