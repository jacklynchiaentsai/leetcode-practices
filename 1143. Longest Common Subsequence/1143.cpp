/*
multi-dimensional dynamic programming
time: O(m*n)
space: O(m*n)
*/
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length(), n = text2.length();
        // lcs[i][j] stores lcs value with text1 from [0,i-1], text2 from[0,j-1]
        vector<vector<int>> lcs(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i<= m; i++){
            for(int j = 1; j<=n; j++){
                // possible routes the current value comes from
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]);
                if (text1[i-1] == text2[j-1])
                    lcs[i][j] = max(lcs[i][j], lcs[i-1][j-1] + 1);
            }
        }

        return lcs[m][n];
    }
};
