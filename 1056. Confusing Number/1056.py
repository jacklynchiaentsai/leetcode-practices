"""
k: number of digits in n
time: O(k) 
space: O(k)
"""

class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid_list = [2,3,4,5,7]
        digit_map = {0:0, 1:1, 6:9, 8:8, 9:6}
        rotated_str = ""
        n_copy = n

        if n ==0:
            return False

        while int(n_copy) > 0:
            digit = n_copy % 10
            n_copy = int(n_copy / 10) 
            if digit in invalid_list:
                return False

            rotated_str += str(digit_map[digit])
    
        if int(rotated_str) == n:
            return False
        else:
            return True
