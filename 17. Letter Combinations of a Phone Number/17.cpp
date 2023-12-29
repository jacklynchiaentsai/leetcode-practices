/*
recursion 
N: length of string digits
time: O(4^N * N) = # of paths * time cost of one path
-> 4^N final solutions each N characters
space: O(N) 
-> for each recursive path need to build each character one at a time

*/

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> combos;
        unordered_map <char, string> digit_map = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"},
        };

        // special case
        if (digits.length() == 0)
            return combos;
        
        genstring(digits, "", combos, digit_map);
        return combos;

    }
    
    // doesn't need to return anything just add answer to vector
    void genstring(string dig_string, string cur_string, vector<string>& combos, unordered_map <char, string> digit_map){
        // base case
        if (dig_string.length() == 0){
            combos.push_back(cur_string);
            return;
        }

        // extract digit character to translate 
        char digit = dig_string[0];
        for(char letter: digit_map[digit]){
            if (dig_string.length() == 1){
                genstring("", cur_string + letter, combos, digit_map);
            } else{
                genstring(dig_string.substr(1), cur_string + letter, combos, digit_map);
            }
        }

    }
};
