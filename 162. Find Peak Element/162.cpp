// binary search: narrowing down scope by one half each time
// view the array as a series of ascending and descending sequences
// time: O(log(n)) space: O(1)
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while(left < right){
            int mid = left + (right-left) / 2; // avoid overflow
            // the middle element is part of a descending sequence
            if (nums[mid]> nums[mid+1]){
                right = mid;
            } else{ // part of an ascending sequence
                left = mid + 1;
            }
        }

        return left;
    }
};
