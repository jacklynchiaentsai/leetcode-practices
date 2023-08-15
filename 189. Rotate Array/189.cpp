class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // when supposed to do nothing reversing it will cause error
        if (nums.size() == 1 || k == 0)
            return;

        // finding pattern
        int steps = k % nums.size();
        
        if (steps == 0)
            return;
        
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin()+steps);
        reverse(nums.begin()+steps, nums.end());
        
    }
};
