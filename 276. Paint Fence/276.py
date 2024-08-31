"""
bottom up dynamic programming
time: O(n)
space: O(n)
"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        elif n == 2:
            return k*k

        # note index start from 0
        numWays = [-1] * n

        # define base case
        numWays[0] = k
        numWays[1] = k * k

        for i in range(2, n):
            numWays[i] = numWays[i - 1] * (k - 1) + numWays[i - 2] * (k - 1)

        return numWays[n - 1]
