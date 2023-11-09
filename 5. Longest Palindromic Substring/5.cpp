// dynamic programming
// gradually expanding outward, checking if inside is palindromic substring
// time: O(n^2) space: O(n^2)
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        
        int start = 0, end = 0;

        for(int i = n-1; i >= 0; i--){
            for(int j = i+1; j<n; j++){
                if (s[i] == s[j]){
                    if ((j-i) <=2 || dp[i+1][j-1]){
                        dp[i][j] = true;

                        if ((j-i) > (end- start)){
                            start = i;
                            end = j;
                        }
                    }
                }
            }
        }

        return s.substr(start, end-start + 1);
    }

};
