class Solution {
public:
    bool canBeEqual(string s1, string s2) {
        if (s1.compare(s2) == 0)
            return true;
        // can only swap 0,2 1,3
        
        string s3 = s1;
        // swap 0,2
        char temp = s3[0];
        s3[0] = s3[2];
        s3[2] = temp;
        if (s3.compare(s2) == 0)
            return true;
        
        string s4 = s1;
        temp = s4[1];
        s4[1] = s4[3];
        s4[3] = temp;
        if (s4.compare(s2) == 0)
            return true;
        
        temp = s3[1];
        s3[1] = s3[3];
        s3[3] = temp;
        if (s3.compare(s2) == 0)
            return true;
        
        return false;
        
    }
};
