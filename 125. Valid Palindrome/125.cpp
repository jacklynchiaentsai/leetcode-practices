class Solution {
public:
    bool isPalindrome(string s) {
        string cpy = "";

        // convert to lowercase and removing non-aplphanumeric characters
        for(int i=0; i<s.length(); i++){
            if (isalpha(s[i])){
                cpy+= tolower(s[i]);
            } else if (isdigit(s[i])){
                cpy += s[i];
            }
        }

        // special case of empty string
        if (cpy.length() == 0)
            return true;
        
        int frontindex = 0, backindex = cpy.length()-1;

        while (frontindex <= backindex){
            if (cpy[frontindex++] != cpy[backindex--]){
                return false;
            }
        }

        return true;
    }
};
