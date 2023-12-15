// dynamic programming
// time: O(n^2)
// space: O(n)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int ans = 1;
        // stores the length of longest increasing subsequence ending at index i
        // initialize with 1 each one is it's own increasing subsequence
        vector<int> maxlen(nums.size(), 1);

        for(int i =0; i< nums.size(); i++){
            int curnum = nums[i];

            // trace back to find longest existing subsequence that ends at a value smaller than curnum
            for(int j = i-1; j>=0; j--){
                if (nums[j] < curnum){
                    maxlen[i] = max(maxlen[i], maxlen[j] + 1);
                }
            }
        }

        // find the longest length
        for(int len: maxlen){
            ans = max(ans, len);
        }

        return ans;
    }
};
