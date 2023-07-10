class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> nmap;
        int left=0, right=0, maxlen = 0;
        while (right < s.length()){
            // if item doesn't yet exist
            if (nmap.find(s[right]) == nmap.end() || nmap[s[right]] == 0){
                nmap[s[right]] = 1;
                maxlen = max(maxlen, right-left+1);
            } else if (nmap[s[right]] == 1){
                while (nmap[s[right]] >0){
                    nmap[s[left]] -= 1;
                    left++;
                }
                nmap[s[right]] = 1;
            }
            right++;
        }
        return maxlen;
    }
};
