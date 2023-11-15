// palindrome has O(n) potential centers but O(n^2) bounds
// math + evaluating palindromes from center outwards
// time: O(n^2) space: O(1)
class Solution {
public:
    // returns length of longest palindromic substring centered at [start, end]
    int expand(int start, int end, string str){
        while (start >= 0 && end < str.length()){
            if (str[start] != str[end]){
                break;
            }
            start--;
            end++;
        }
        // while loop ends when the characters are different -> neglect them
        return (end - 1) - (start + 1) + 1;
    }
    string longestPalindrome(string s) {
        // keeps track of index bounds of longest palindromic substring
        int startindex = 0, endindex = 0;
        int dist;
        for(int i = 0; i < s.length(); i++){
            int oddlen = expand(i,i,s);
            if (oddlen > (endindex - startindex + 1)){
                dist = oddlen / 2; // take floor value
                startindex = i - dist;
                endindex = i + dist;
            }

            int evenlen = expand(i, i+1, s);
            if (evenlen > (endindex - startindex + 1)){
                dist = evenlen / 2;
                startindex = i - dist + 1;
                endindex = i + dist;
            }
        }

        return s.substr(startindex, endindex - startindex + 1);
    }
};
