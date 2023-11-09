// if the string is continuous then we generate string.length() amount of homogenous substrings 
// time: O(N) space: O(N) longest possible length of curstring
class Solution {
public:
    int countHomogenous(string s) {
        int tot = 0;
        int mod = 1e9 + 7;
        string curstring = "";
        for (char ch: s){
            if (curstring.length() == 0 || ch != curstring[0]){
                curstring = ch;
                tot = (tot + 1) % mod;
            } else{
                curstring+= ch;
                tot = (tot + curstring.length())  % mod;
            }
        }

        return tot;
    }
};
