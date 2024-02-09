// time: O(n) n = length of haystack
// space: O(1)
class Solution {
public:
    int strStr(string haystack, string needle) {
        int ans = haystack.find(needle);
        if (ans == string::npos)
            return -1;
        else
            return ans;
    }
};
