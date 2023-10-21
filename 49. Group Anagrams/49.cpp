// L = maximum length of string
// time: O(n*Llog(L)) space: O(n*L) stored in map
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // categorize by sorted string
        unordered_map<string, vector<string>> anagram_map;
        for(string str: strs){
            string sorted = str;
            sort(sorted.begin(), sorted.end());
            anagram_map[sorted].push_back(str);
        }

        vector<vector<string>> groups;
        for(auto it: anagram_map){
            groups.push_back(it.second);
        }

        return groups;
    }
};
