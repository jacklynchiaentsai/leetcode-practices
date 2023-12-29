/*
dynamic programming: dp[i] maximum subarray sum ending at index i
time: O(N) 
space: O(N)
*/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        int maxsum = dp[0];

        for(int i =1; i< nums.size(); i++){
            dp[i] = max(nums[i], nums[i] + dp[i-1]);
            maxsum = max(maxsum, dp[i]);
        }

        return maxsum;

    }
};
