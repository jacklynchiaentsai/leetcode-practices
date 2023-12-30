/*
bottom up dynamic programming: recursion & memoization
N: number of elements in nums
maxNum: largest number in nums
time: O(N+ maxNum) : iteration of nums + recursion
space: O(N)
*/
/*
key observations:
- order does not matter
- if I delete an element, might as well take all elements of same value because "every" neighboring value would be deleted

dp process:
- I should define states as the value I am choosing
- If I pick current element I cannot pick the value from val - 1
*/
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        unordered_map<int, int> points;
        int maxNum = -1;
        // first calculate frequency of element
        for(int num: nums){
            points[num] += 1;
            maxNum = max(maxNum, num);
        }

        // update map to total value of deleting that element val
        for(auto it: points){
            int key = it.first;
            int val = it.second;
            points[key] = key * val;
        }

        // initialization (only depends on two previous value so only need two vars)
        int twoBack = 0;
        int oneBack = points[1];
        int maxpoints = oneBack;

        for(int i=2; i< maxNum + 1; i++){
           maxpoints = max(points[i] + twoBack, oneBack);
           twoBack = oneBack;
           oneBack = maxpoints;
        }

        return maxpoints;
    }
};
