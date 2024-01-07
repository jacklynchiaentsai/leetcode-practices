/*
no sorting solution, use set to keep track of values that I've seen
time: O(n^2)
space: O(n)
*/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> ans_set;
        unordered_set<int> pivot_set;
        unordered_set<int> seen_vals;

        for(int i =0; i< nums.size(); i++){
            // seen this pivot before
            if (pivot_set.find(nums[i]) != pivot_set.end()){
                continue;
            }
            pivot_set.insert(nums[i]);

            seen_vals.clear();
            for(int j = i+1; j< nums.size(); j++){
                int kval = -nums[i] - nums[j];
                if (seen_vals.find(kval) != seen_vals.end()){
                    vector<int> triplet = {nums[i], nums[j], kval};
                    sort(triplet.begin(), triplet.end());
                    ans_set.insert(triplet);
                }
                seen_vals.insert(nums[j]); // avoid double usage
            }

        }
        
        vector<vector<int>> ans(ans_set.begin(), ans_set.end());
        return ans;
    }
};
/*
- order of output and order of triplets does not matter
*/
