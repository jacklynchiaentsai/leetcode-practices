// top down dynamic programming
// n: length of s, m: dictionary length, k: average length of words in wordDict
// time: O(n*m*k) -> k is due to substr function
// space: O(n) for memo
class Solution {
public:
    // array that stores dp value for each index (also works as cache)
    // use int because want to check: hasn't been computed, false, or true
    vector<int> memo;
    // returns whether it is possible to build s up to and including index i
    bool dp(int i, string s, vector<string> wordDict){
        // base case empty string 
        if (i < 0)
            return true;
        
        // return saved value in cache to avoid duplicate calculation
        if (memo[i] != -1){
            return (memo[i] == 1);
        }

        // iterate through every word in dictionary to find if there is a word that ends at index i
        for(string word: wordDict){
            int wordlen = word.length();
            
            // handle out of bounds
            // (i - wordlen + 1) is the starting index of word
            if ((i - wordlen + 1) < 0)
                continue;
            
            // found matching word
            if (s.substr(i-wordlen+1, wordlen).compare(word) == 0){
                // check if the substring before word is also buildable
                if (dp(i-wordlen, s, wordDict)){
                    memo[i] = 1;
                    return true;
                }
            }
        }

        memo[i] = 0;
        return false;

    }
    bool wordBreak(string s, vector<string>& wordDict) {
        // initializing global variables
        memo = vector<int>(s.length(), -1);
        return dp(s.length() - 1, s, wordDict);
    }
};
