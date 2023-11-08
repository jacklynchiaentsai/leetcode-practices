// two stack method: stack because I want to process later first
// N: length of string K: number that appeared in string
// time: (N* maxK) space: O(N)
class Solution {
public:
    string decodeString(string s) {
        stack<string> str_stack;
        stack<int> num_stack;

        string cur_num = "";
        string cur_string = "";

        for (char ch: s){
            if (ch == '['){
                num_stack.push(stoi(cur_num));
                str_stack.push(cur_string);
                cur_num = "";
                cur_string = "";
            } else if (ch == ']'){
                int counts = num_stack.top();
                num_stack.pop();
                string decoded_string = "";
                for (int i =0; i< counts; i++){
                    decoded_string += cur_string;
                }
                string new_string = str_stack.top();
                str_stack.pop();
                cur_string = new_string + decoded_string;
            } else if (isalpha(ch)){
                cur_string += ch;
            } else {
                cur_num += ch;
            }
        }

        return cur_string;
    }
};
