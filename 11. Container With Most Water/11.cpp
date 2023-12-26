// two pointer approach
// start with max width so the only thing limiting is height
// update the limiting height to find better solution
// time: O(N)
// space: O(1)

class Solution {
public:
    int maxArea(vector<int>& height) {
        int start = 0, end = height.size()- 1;
        int maxval = 0;
        while(start < end){
            int temp = min(height[start], height[end]) * (end - start);
            
            if (temp > maxval)
                maxval = temp;
            
            if (height[start] <= height[end]){
                start++;
            } else{
                end--;
            }
        }
        return maxval;
    }
};
