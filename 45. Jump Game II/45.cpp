/*
Greedy solution
- guaranteed solution
- if we can already reach index i in the (j-1)th jump, don't consider it in the jth jump otherwise it would take more steps

- time: O(N)
- space: O(1)
*/
class Solution {
public:
    int jump(vector<int>& nums) {
        // end: furthest starting index of the current jump from all the indices Im jumping from
        // far: furthest reachable index of the current jump
        int end = 0, far = 0, steps = 0;

        // don't need to consider the last index
        for(int i =0; i < nums.size() - 1; i++){
            far = max(far, i + nums[i]);

            // finished the range of this jump, move on to the starting range of the next jump
            if (i == end){
                steps++;
                end = far; // won't end the next jump until I reached the furthest possible starting point of current jump
            }
        }
        return steps;
    }
};
