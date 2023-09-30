// time: O(nlogn) from sorting
// space: O(1)

class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int n = skill.size();
        sort(skill.begin(), skill.end());
        long long int chemistry = 0;
        int skillval = skill[0] + skill[n-1];
        for(int i=0; i< n/2; i++){
            if (skill[i] + skill[n-1-i] != skillval)
                return -1;
            
            chemistry += skill[i] * skill[n-1-i];
        }

        return chemistry;
    }
};
