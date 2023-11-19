// time: O(nlogn)
class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        // number of operations for n = gap of distinct nums between min and n
        int distinctnums = 0;
        // keeps track of previous number in the case of identical values
        int prevnum= nums[0]; 
        int numops = 0;
        
        for(int num: nums){
            if (num == prevnum){
                numops += distinctnums;
            } else{
                distinctnums++;
                numops += distinctnums;
                prevnum = num;
            }
        }
        return numops;
    }
};
