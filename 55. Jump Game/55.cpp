/*
top down dynamic programming problem with memoization
time: O(N^2)
space: O(N)
*/
class Solution {
public:
    bool canJump(vector<int>& nums) {
        // stores if this index is reachable, initialize as -1 to indicate unvisited
        vector<int> reachable(nums.size(), -1);
        reachable[0] = 1;

        return canReach(nums.size()-1, nums, reachable);
    }

    // returns array of starting indices that can reach the targetindex
    bool canReach(int targetindex, vector<int>& nums, vector<int>& reachable){
        if (targetindex == 0)
            return true;
        
        for(int i =0; i< targetindex; i++){
            if (i + nums[i] >= targetindex){
                if (reachable[i] == 1){
                    return true;
                } else if (reachable[i] == -1){
                    if (canReach(i, nums, reachable)){
                        reachable[i] = 1;
                        return true;
                    } else{
                        reachable[i] = 0;
                    }
                }
            }
        }

        return false;
    }
};
