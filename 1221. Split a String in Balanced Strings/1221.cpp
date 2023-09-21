// greedy soltution time: O(n) space O(1)
// any split of a balanced string the remaining will also be a balanced string
// split as many times as possible every time running into a balanced string
class Solution {
public:
    int balancedStringSplit(string s) {
        int balance = 0;
        int count = 0;
        for (char ch: s){
            if (ch == 'R')
                balance++;
            else
                balance--;
            
            if (balance == 0)
                count++;
        }

        return count;
    }
};
