"""
bottom up dynamic programming (state machines)
time: O(n)
space: O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [[-1, -1] for _ in range (len(prices))]
        profits[0][0] = 0
        profits[0][1] = -prices[0]

        for i in range(1, len(prices)):
            profits[i][0] = max(profits[i-1][0], profits[i-1][1] + prices[i])
            profits[i][1] = max(profits[i-1][1], profits[i-1][0] - prices[i])

        return profits[len(prices) -1][0]

        

"""
profits[i][0 or 1]

profits[i][0] = max(profit[i-1][0], profit[i-1][1] + prices[i])
profits[i][1] = max(profit[i-1][1], profit[i-1][0] - prices[i])
maxprofit = profits[len(prices) - 1][0]
ith day
buy, sell, or do nothing --> 0 or 1 stock share left after the action on ith day
"""
