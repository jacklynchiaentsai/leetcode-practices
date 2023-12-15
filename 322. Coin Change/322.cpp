// n = coins.size() m = amount
// time: O(n*m)
// space: O(m)
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // array that stores the number of coins to make up amount = index
        // not possible to achieve amount with amount + 1 coins so set that as max value
        vector<int> numcoins(amount + 1, amount + 1);
        //initialize
        numcoins[0] = 0;

        // dynamic programming: latter combinations might yield better answer
        for (int coin: coins){
            // infinite coins: start from coin to amount, can accumulate
            // note: limited coins start backwards
            for (int i = coin; i <= amount; i++){
                numcoins[i] = min(numcoins[i], numcoins[i-coin] + 1);
            }
        }

        if (numcoins[amount] == amount + 1)
            return -1;
        else
            return numcoins[amount];
    }
};
