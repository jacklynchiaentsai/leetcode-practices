/*
because we are sorting with the starting point, we can guarantee the following scenarios of the next point:
- overlap with longer ending point
- within range of previous point -> in this case we do not need to update
- completely no intersection to the right of the curent range

we need to keep track of the ending point
*/
class Solution {
public:
    int numberOfPoints(vector<vector<int>>& nums) {
        // customized lambda comparison function
        auto comparator = [] (vector<int>& a, vector<int>& b) {return a[0] < b[0];};
        sort(nums.begin(), nums.end(), comparator);

        int points = 0, current = 0;

        for(auto range: nums){
            // completely no intersection to the right of the cuurent range
            if (range[0] > current){
                points += range[1]-range[0] + 1;
            } 
            // overlap with longer ending point
            else if (range[1] > current){
                points += range[1] - current;
            }

            current = max(current, range[1]);
        }

        return points;
    }
};
