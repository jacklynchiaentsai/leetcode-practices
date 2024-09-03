# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from collections import deque
"""
time: O(n)
space: O(1)
logical deduction (similar to Ellen's 2 pick 1 game)
- there could only be 1 or 0 celebrity
- at each API call we can successfully eliminate 1, whoever stays till the last is the celebrity candidate
- only need to check for full condition for the celebrity candidate
"""
class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0

        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i

        # double check if the person is a celebrity
        for i in range(n):
            if i == celebrity:
                continue
            
            # only need to check for both directions for 1 candidate
            if knows(celebrity, i) or not knows(i, celebrity):
                return -1

        return celebrity



                
