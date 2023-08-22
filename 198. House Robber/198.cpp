class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size()==1)
            return nums[0];
        else if (nums.size()==2)
            return max(nums[0], nums[1]);

        int rob[nums.size()];
        memset(rob, 0, sizeof(rob));
        rob[0] = nums[0];
        rob[1] = max(nums[0], nums[1]);
        for(int i = 2; i < nums.size(); i++){
            rob[i] = max(nums[i] + rob[i-2], rob[i-1]);
        }

        return rob[nums.size()-1];
    }
};
