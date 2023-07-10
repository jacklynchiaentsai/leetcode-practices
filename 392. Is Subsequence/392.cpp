class Solution {
public:
    bool isSubsequence(string s, string t) {
        // special case
        if (s.length() == 0)
            return true;

        int sindex = 0;
        for (int i=0; i< t.length(); i++){
            if (t[i] == s[sindex]){
                sindex++;
                if (sindex == s.length())
                    return true;
            }
        }

        return false;
    }
};
