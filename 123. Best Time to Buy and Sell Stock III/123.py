"""
dynamic programming: state machines 
time: O(n)
space: O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MIN_VAL = float('-inf')
        maxprofit = [[[MIN_VAL, MIN_VAL] for _ in range(3)] for x in range(len(prices))]
        # print(len(maxprofit))
        # print(len(maxprofit[0]))
        # print(len(maxprofit[0][0]))
        
        # base cases
        maxprofit[0][0][0] = 0
        maxprofit[0][1][1] = -prices[0]

        for i in range(1, len(prices)):
            maxprofit[i][0][0] = 0

            # considering transactions 1 and 2
            for num in range(1,3):
                maxprofit[i][num][0] = max(maxprofit[i-1][num][1] + prices[i], maxprofit[i-1][num][0])
                maxprofit[i][num][1] = max(maxprofit[i-1][num - 1][0] - prices[i], maxprofit[i-1][num][1])

        # sometimes it might be better not to trade so consider all possible transaction numbers
        return max(maxprofit[len(prices) - 1][0][0], max(maxprofit[len(prices) - 1][2][0], maxprofit[len(prices) - 1][1][0]))

"""
a transaction is counted as buy + sell
- additional constraint: number of transactions
- the original at most hold one stock still holds
maxprofit[i][0th or 1st or 2nd transaction][0 or 1 stocks lefet after action]

base cases
maxprofit[0][0][0] = 0
maxprofit[0][1][1] = -price[i]

transitions
maxprofit[i][0][0] = 0
maxprofit[i][1][0] = max(maxprofit[i-1][1][1] + price[i], maxprofit[i-1][1][0])
maxprofit[i][1][1] = max(maxprofit[i-1][0][0] - price[i], maxprofit[i-1][1][1])
maxprofit[i][2][0] = max(maxprofit[i-1][2][1] + price[i], maxprofit[i-1][2][0])
"""
