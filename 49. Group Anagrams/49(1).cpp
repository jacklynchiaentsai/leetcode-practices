// L = maximum length of string
// time: O(n*L) space: O(n*L) stored in map
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // categorize by alphabetical count
        // lowercase letters -> fixed count of 26 -> form unique key
        unordered_map<string, vector<string>> anagram_map;
        for(string str: strs){
           int letter_count[26];
           memset(letter_count, 0, sizeof(letter_count));
           
           // counting the letter occurences
           for (char ch: str){
               int index = ch - 'a';
               letter_count[index] += 1;
           }

           // creating unique string key (constant time)
           string key = "";
           for (int i =0; i< 26; i++){
               // adding delimeter to avoid 1,11 and 11,1 cases
               key += to_string(letter_count[i]) + ",";
           }
           
           anagram_map[key].push_back(str);
        }

        vector<vector<string>> groups;
        for(auto it: anagram_map){
            groups.push_back(it.second);
        }

        return groups;
    }
};
