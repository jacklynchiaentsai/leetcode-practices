// bottom up dynamic programming: start from i no recursion
// n: length of s, m: dictionary length, k: average length of words in wordDict
// time: O(n*m*k)
// space: O(n)
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // stores whether it is possible to build s up to and including index i
        vector<bool> dp(s.length(), false);

        // iterate from bottom up
        for(int i =0; i < s.length(); i++){
            // iterate through every word in dictionary to find if there is word that ends at index i
            for(string word: wordDict){
                int wordlen = word.length();

                if ((i- wordlen+1) < 0)
                    continue;
                
                if (s.substr(i-wordlen+1, wordlen).compare(word) == 0){
                    // consider the case when there is no substring before word in s up to index i
                    if ((i-wordlen) == -1){
                        dp[i] = true;
                    }
                    // check if the substring before word is also buildable
                    else if (dp[i-wordlen]){
                        dp[i] = true;
                    }
                }
            }
        }

        return dp[s.length()-1];
    }
};
