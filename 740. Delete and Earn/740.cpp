/*
top-down dynamic programming: recursion & memoization
N: number of elements in nums
maxNum: largest number in nums
time: O(N+ maxNum) : iteration of nums + recursion
space: O(N+maxNum)
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
        unordered_map<int, int> maxpoint_cache;
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

        return maxPoints(maxNum, points, maxpoint_cache);

    }

    int maxPoints(int num, unordered_map<int, int>& points, unordered_map<int, int>& maxpoint_cache){
        // base cases
        if (num == 0)
            return 0;
        if (num == 1)
            return points[1];
        
        if(maxpoint_cache.find(num) != maxpoint_cache.end())
            return maxpoint_cache[num];
        else{
            // store solution
            maxpoint_cache[num] = max(points[num] + maxPoints(num-2, points, maxpoint_cache), maxPoints(num-1, points, maxpoint_cache));
            return maxpoint_cache[num];
        }
            
    }
};
