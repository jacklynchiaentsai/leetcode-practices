// improve space complexity to O(1) by directly modifying the s string
// two pointer swap approach
// time: O(n) space: O(1)
class Solution {
public:
    string reverseWords(string s) {
        int startindex = 0;
        for(int i = 0; i< s.length(); i++){
            if (s[i] == ' ' || i == s.length() - 1){
                // consider the last word
                int endindex;
                if (i == s.length()- 1){
                    endindex = i;
                } else{
                    endindex = i-1;
                }

                char temp;
                while(startindex < endindex){
                    temp = s[startindex];
                    s[startindex] = s[endindex];
                    s[endindex] = temp;
                    startindex++;
                    endindex--;
                }
                startindex = i+1;
            }
        }
        return s;
    }
};
