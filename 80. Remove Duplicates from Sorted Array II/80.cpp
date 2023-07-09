class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        auto it = nums.begin();
        int count = 0;
        int curr = nums[0];
        while(it != nums.end()) {
            if (curr == *it && count >= 2){
                it = nums.erase(it, upper_bound(nums.begin(), nums.end(), *it));
            } else if (curr == *it && count < 2){
                count++;
                it++;
            } else if (curr != *it){
                count = 1; 
                curr = *it;
                it++;
            }
        }
        return nums.size();
    };
};
