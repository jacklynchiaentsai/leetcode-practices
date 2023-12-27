/*
the way to gain maximum profit is by getting the profit every time possible
time: O(N)
space: O(1)
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // stores the indices of current maximum and minimum positions
        int curmin = 0, curmax = 0;
        int profit = 0;
        for(int i =0; i < prices.size(); i++){
            int curprice = prices[i];
            // found higher peak
            if (curprice > prices[curmax]){
                curmax = i;
            } else if (curprice < prices[curmax]){ // found valley
                profit += prices[curmax] - prices[curmin];
                curmin = i;
                curmax = i; // restart searching from current valley
            }
        }

        // make sure to record the last proft
        profit += prices[curmax] - prices[curmin];
        return profit;
    }
};
