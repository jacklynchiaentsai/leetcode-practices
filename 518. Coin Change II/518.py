"""
dynamic programming (bottom up)
n = len(coins)
m = amount
time: O(mn)
space: O(m)
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, len(dp)):
                if (i-coin) >= 0:
                    dp[i] += dp[i-coin]

        return dp[amount]
"""
dynamic programming
dp[i] = number of ways I can make up amount i
-> i should range from 0 to amount

initialization:
dp[0] = 1
dp[i for every other value than 0] = 0 

for each coin:
    iterate from i is 1 up to len(dp):
        dp[i] = dp[i] + dp[i-coin]
        -> check for index out of bounds

return dp[amount]
    
"""
