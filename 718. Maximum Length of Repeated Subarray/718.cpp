// dynamic programming but has to be continuous
// can only update diagonally
// time: O(m*n) space: O(m*n)
class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        int lcs[m+1][n+1];
        memset(lcs, 0, sizeof(lcs));
        int ans = 0;
        // i, j represents index in each array
        for(int i = 0; i< m; i++){
            for(int j = 0; j < n; j++){
                if (nums1[i] == nums2[j]){
                    lcs[i+1][j+1] = lcs[i][j] + 1;
                    ans = max(ans, lcs[i+1][j+1]);
                } 
            }
        }

        return ans;
    }
};
