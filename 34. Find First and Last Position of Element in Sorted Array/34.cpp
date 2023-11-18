// time: O(log(n)) space: O(1)
// two binary searches: one searching for first position of element the other searching for last position
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans;
        // searching for first position
        int lower = 0, upper = nums.size() - 1;
        // can exist the case with only one element existing in array
        while (lower <= upper){
            int mid = lower + (upper-lower) / 2;
            if (nums[mid] == target){
                // first conditional checks if it is the only element in array -> avoid out of bounds
                if ((mid == lower) || (nums[mid] != nums[mid - 1])){
                    ans.push_back(mid);
                    break;
                } else{ // remove upper half
                    upper = mid - 1;
                }
            } else if (nums[mid] > target){
                upper = mid - 1;
            } else{
                lower = mid + 1;
            }
        }
        // didn't find any element 
        if (ans.size() == 0){
            ans.push_back(-1);
            ans.push_back(-1);
            return ans;
        }

        // searching for last position
        lower = ans[0];
        upper = nums.size() - 1;
        while (lower <= upper){
            int mid = lower + (upper-lower) / 2;
            if (nums[mid] == target){
                // first conditional checks if it is the only element in array -> avoid out of bounds
                if ((mid == upper) || (nums[mid] != nums[mid + 1])){
                    ans.push_back(mid);
                    break;
                } else{ // remove lower half
                    lower = mid + 1;
                }
            } else if (nums[mid] > target){
                upper = mid - 1;
            } else{
                lower = mid + 1;
            }
        }

        return ans;
    }
};
