/*
can only consider larger values after current min value
time: O(N)
space: O(1)
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minprice = INT_MAX;
        int ans = 0;
        for(int price: prices){
            minprice = min(minprice, price);
            ans = max(ans, price - minprice);
        }
        return ans;
    }
};
