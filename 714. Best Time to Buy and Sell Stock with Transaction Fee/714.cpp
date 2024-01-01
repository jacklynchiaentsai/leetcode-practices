/*
dynamic programming: state machine
time: O(N)
space: O(N)
*/
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        // profit[i][0]: the maximum profit when I have 0 stocks at hand after day i action
        vector<vector<int>> profit(prices.size(), vector<int>(2));
        profit[0][0] = 0;
        profit[0][1] = -prices[0] - fee;

        for(int i = 1; i< prices.size();i++){
            profit[i][0] = max(profit[i-1][0], profit[i-1][1] + prices[i]);
            profit[i][1] = max(profit[i-1][1], profit[i-1][0] - prices[i] - fee);
        }

        return profit[prices.size()-1][0];
    }
};
