/*
dynamic programming: dp[i] maximum subarray sum ending at index i
time: O(N) 
space: O(1)
*/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cursum = nums[0];
        int maxsum = cursum;

        for(int i =1; i< nums.size(); i++){
           if (cursum < 0)
            cursum = 0;
           cursum += nums[i];
           maxsum = max(cursum, maxsum);
        }

        return maxsum;

    }
};
