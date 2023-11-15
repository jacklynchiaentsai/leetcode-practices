// time: O(n) space: O(n)
class Solution {
public:
    string reverseWords(string s) {
        string ans = "";
        // splitting words by whitespace and reversing each individually
        stringstream ss(s);
        string tmp;

        while (ss>> tmp){  
            reverse(tmp.begin(), tmp.end());
            ans += tmp + " ";
        }
        // remove extra whitspace
        return ans.substr(0, ans.length()-1);
    }
};
