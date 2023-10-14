// divide and conquer recongnize repeating patterns
// checking for edge cases, building helper functions and using instance vars
// time: O(N), space: O(N)
class Solution {
public:
    unordered_map<char, string> ones= {
        {'1', "One"},
        {'2', "Two"},
        {'3', "Three"},
        {'4', "Four"},
        {'5', "Five"},
        {'6', "Six"},
        {'7', "Seven"},
        {'8', "Eight"},
        {'9', "Nine"}
    };

    unordered_map<char, string> oneten = {
        {'0', "Ten"},
        {'1', "Eleven"},
        {'2', "Twelve"},
        {'3', "Thirteen"},
        {'4', "Fourteen"},
        {'5', "Fifteen"},
        {'6', "Sixteen"},
        {'7', "Seventeen"},
        {'8', "Eighteen"}, 
        {'9', "Nineteen"}
    };

    unordered_map<char, string> tens = {
        {'2', "Twenty"},
        {'3', "Thirty"},
        {'4', "Forty"},
        {'5', "Fifty"},
        {'6', "Sixty"},
        {'7', "Seventy"},
        {'8', "Eighty"},
        {'9', "Ninety"}
    };

    string threedigits(string num){
        string ans = "";
        char hundreds = num[0], tens = num[1], ones = num[2];
        bool noprev = true;
        if (hundreds != '0'){
            noprev = false;
            ans += this->ones[hundreds] + " Hundred";
        }
        if (tens != '0'){
            if (!noprev)
                ans += " ";

            if (tens == '1'){
                ans += this->oneten[ones];
                return ans;
            } else{
                noprev = false;
                ans += this->tens[tens];
            }
        }

        if (ones != '0'){
            if (!noprev)
                ans += " ";
            ans += this->ones[ones];
        }

        return ans;
    }

    string numberToWords(int num) {
        if (num == 0)
            return "Zero";
        
        string ans = "";
        string numstr = to_string(num);
        // make the length in pairs of three
        while (numstr.length() % 3 != 0){
            numstr = "0" + numstr;
        }
        
        for(int i =0; i< numstr.length(); i+= 3){
            string threes = numstr.substr(i,3);
            ans += threedigits(threes);
            if (threedigits(threes).length() > 0){
                if ((numstr.length() - i) / 3 == 4)
                    ans += " Billion ";
                else if ((numstr.length() - i) / 3 == 3)
                    ans += " Million ";
                else if ((numstr.length() - i) / 3 == 2)
                    ans += " Thousand ";
            }
        }

        // remove extra trailing whitespace
        if (ans[ans.length() - 1] == ' '){
            ans = ans.substr(0, ans.length() - 1);
        }

        return ans;
    }
};
