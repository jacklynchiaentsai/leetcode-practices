// initial key: the net value going in and out of eeach person must be equivalent
// solution reference: https://leetcode.com/problems/optimal-account-balancing/solutions/219187/short-o-n-2-n-dp-solution-with-detailed-explanation-and-complexity-analysis/
// time: O(n * 2^n) space: O(2^N)
// convert problem to: finding maximum number of min_sets
class Solution {
public:
    int minTransfers(vector<vector<int>>& transactions) {
        // net balance is what matters
        unordered_map<int, int> net_balance;
        for (auto transaction: transactions){
            int from_id = transaction[0];
            int to_id = transaction[1];
            int amount = transaction[2];

            net_balance[from_id] -= amount;
            net_balance[to_id] += amount;
        }

        // exclude people whose net balance = 0
        // order doesn't matter in this problem
        vector<int> transaction_set;

        for(auto it: net_balance){
            if (it.second != 0)
                transaction_set.push_back(it.second);
        }

        // bitmask dynamic programming
        int N = transaction_set.size();

        // finding maximum number of min_sets
        int bin_limit = (int)pow(2, N);
        int num_minsets[bin_limit];
        int sum_minsets[bin_limit];

        // initialize
        memset(num_minsets, 0, sizeof(num_minsets));
        memset(sum_minsets, 0, sizeof(sum_minsets));

        // iterating through bit mask values
        for(int submask= 0; submask< bin_limit; submask++){
            int check_bit = 1;
            // using the current i as a submask basis find all masks with 1 more bit difference
            for(int j = 0; j< N; j++){
                // since all other digits are 0 in check_bit, bitwise and is 0 means that the checkbit is at the bit digit of i where the digit == 0 
                if( (submask & check_bit) == 0){
                    int mask = submask | check_bit;
                    // calculating sum: adding the 1 digit difference
                    sum_minsets[mask] = sum_minsets[submask] + transaction_set[N-j-1];
                    check_bit <<= 1;

                    // don't have to iterate through all submasks, just update whenever encounter new submask
                    if (sum_minsets[mask] == 0){
                        num_minsets[mask] = max(num_minsets[mask], num_minsets[submask] + 1);
                    } else{
                        num_minsets[mask] = max(num_minsets[mask], num_minsets[submask]);
                    }
                }
            }

        }

        int M = num_minsets[bin_limit - 1];

        // in each minset need len(minset) - 1 transactions to settle debt
        return N-M;
    }
};
