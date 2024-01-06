/*
TLE Solution: top down DP
time: O(n^2)
space: O(n)
*/
class Solution {
public:
    int minjumps;

    void canReach(int curindex, int steps, vector<int>& nums){
        if (curindex == 0){
            minjumps = min(minjumps, steps);
            return;
        }

        for(int i =0; i< curindex; i++){
            if (i + nums[i] >= curindex){
                canReach(i, steps + 1, nums);
            }
        }
    }

    int jump(vector<int>& nums) {
        int n = nums.size();
        minjumps = n;
        canReach(n-1, 0, nums);
        return minjumps;
    }
};
