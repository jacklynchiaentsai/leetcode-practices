// two stack strategy
// time: O(n) space: O(n)
class Solution {
public:
    int calculate(string s) {
        // applying parentheses to beginning and end of string
        string str = "(" + s + ")";
        string cur_num = "";
        stack<string> num_st;
        stack<char> op_st;
        bool checkneg = false;
        for (char ch: str){
            if (ch == '('){
                string temp = "";
                temp += ch;
                num_st.push(temp);
                // prepending operator before each number for calc convenience
                op_st.push('+'); 
                checkneg = true;
            } else if (isdigit(ch)){
                checkneg = false;
                cur_num += ch;
            } else if (ch == ' '){
                if (cur_num.length() > 0){
                    num_st.push(cur_num);
                    cur_num = "";
                }
            } else if (ch == '+' || ch == '-'){
                if (cur_num.length() > 0){
                    num_st.push(cur_num);
                    cur_num = "";
                }

                if (checkneg){
                    op_st.pop(); // pop out the preassumed "+"
                }
                op_st.push(ch);
            } else { // ch == ')'
                
                if (cur_num.length() > 0){
                    num_st.push(cur_num);
                    cur_num = "";
                }
                
                // evaluate value in parentheses
                int cur_val = 0; 
                while(!num_st.empty()){
                    string num = num_st.top();
                    num_st.pop();

                    if (num.compare("(") == 0){
                        num_st.push(to_string(cur_val));
                        break;
                    }

                    char op = op_st.top();
                    op_st.pop();

                    if (op == '-'){
                        cur_val -= stoi(num);
                    } else{
                        cur_val += stoi(num);
                    }

                }
            }
        }

        return stoi(num_st.top());
    }
};
