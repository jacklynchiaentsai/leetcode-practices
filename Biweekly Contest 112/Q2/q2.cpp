class Solution {
public:
    bool checkStrings(string s1, string s2) {
        unordered_map <string, int> s1_map;
        unordered_map <string, int> s2_map;
        int n = s1.length();
        string temp = "";
        
        for(int i = 0; i< n; i++){
            temp = s1[i];
            if (i%2 == 0)
                temp += "e";
            else
                temp += "o";
            
            if (!s1_map.count(temp))
                s1_map[temp] = 1;
            else
                s1_map[temp] += 1;
        }
        
        for(int i = 0; i< n; i++){
            temp = s2[i];
            if (i%2 == 0)
                temp += "e";
            else
                temp += "o";
            
            if (!s2_map.count(temp))
                s2_map[temp] = 1;
            else
                s2_map[temp] += 1;
        }
        
        for(auto it: s1_map){
            string keypair = it.first;
            if (it.second != s2_map[keypair])
                return false;
        }
        
        return true;
        
    }
};
