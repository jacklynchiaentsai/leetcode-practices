"""
keep track of lowest price seen
time: O(n)
space: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]

        for price in prices:

            if price < min_price:
                min_price = price
            else:
                profit = max(profit, price - min_price)
        
        return profit
