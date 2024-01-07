/*
sort -> pivot point iteration + two pointer for two sum
time: O(n^2)
space: O(n)
*/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> ans_set;

        sort(nums.begin(), nums.end());
        // assume i < j < k
        for(int i =0; i < nums.size(); i++){
            if (nums[i] > 0){
                break;
            }

            int start = i+1, end = nums.size() - 1;
            while (start < end){
                int cursum = nums[start] + nums[end] + nums[i];
                if (cursum ==0){
                    vector<int> triplet = {nums[start], nums[end], nums[i]};
                    sort(triplet.begin(), triplet.end());
                    ans_set.insert(triplet);
                }
                
                if (cursum < 0 || cursum ==0){
                    while((start+1) < nums.size() && nums[start] == nums[start+1]){
                        start++;
                    } 
                    start++;
                } 
                
                if (cursum > 0 || cursum ==0){
                    while((end - 1) > start && nums[end] == nums[end-1]){
                        end--;
                    }
                    end--;
                }
            }
        }

        vector<vector<int>> ans(ans_set.begin(), ans_set.end());
        return ans;
    }
};
/*
- order of output and order of triplets does not matter
*/
