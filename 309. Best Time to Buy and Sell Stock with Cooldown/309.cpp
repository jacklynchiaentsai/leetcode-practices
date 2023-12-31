/*
state machine dynamic programming (modified with cooldown)
- three possible actions: buy, sell, rest => captured with 0,1
- days => captured with i index

time: O(N)
space: O(N*2) = O(N)
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // profit[i][0] maximum profit on the ith day with 0 stocks in hand after ith day action
        vector<vector<int>> profit(prices.size(), vector<int>(2));

        // initialization of profit at day 0
        profit[0][0] = 0; // resting on the first day
        profit[0][1] = -prices[0]; // buying one stock on the first day

        for(int i = 1; i < prices.size(); i++){
            // continue resting or sell the stock
            profit[i][0] = max(profit[i-1][0], profit[i-1][1] + prices[i]);

            // continue resting or buy the stock
            if (i == 1){
                // not possible to sell on day 0
                profit[i][1] = max(profit[i-1][1], profit[i-1][0] - prices[i]);
            } else{
                // I have no stocks left on i-2 so can't sell on i-1
                profit[i][1] = max(profit[i-1][1], profit[i-2][0] - prices[i]);
            }
            
        }

        // always more profit if we end up with no stocks
        return profit[prices.size()-1][0];
    }
};
