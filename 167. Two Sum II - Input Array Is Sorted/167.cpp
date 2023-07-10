class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // there is exactly one solution
        int left = 0, right = numbers.size() - 1;
        vector<int> ans;
        while (left < right){
            int sum = numbers[left] + numbers[right];
            if (sum == target){
                break;
            } else if (sum > target){
                right--;
            } else{
                left++;
            }
        }

        ans.push_back(left+1);
        ans.push_back(right+1);
        return ans;
    }
};
