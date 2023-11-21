// time: O(n) space: O(n)
// dependant on two nums: x + rev(y) = rev(x) + y
// rearrange: x - rev(x) = y - rev(y)
class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        long long int mod = 1e9 + 7;
        vector<int> diff_arr;
        unordered_map<int, long long int> diff_count;
        long long int nicepairs = 0;
        // compute the reverse of each number
        // simply counting the same difference will overflow so need to save it in separate array first and increment correspondingly
        
        for (int num: nums){
            string num_str = to_string(num);
            reverse(num_str.begin(), num_str.end());
            diff_arr.push_back(num - stoi(num_str));
        }

        for(int diff: diff_arr){
            // strict constraint i< j
            // every occurenece of diff can be paired with existing occurences of diff
            nicepairs = (nicepairs + diff_count[diff]) % mod;
            diff_count[diff]++;
        }

        return nicepairs;
    }
};
