class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> charmap( 
        {{')', '('}, 
        {']', '['}, 
        {'}', '{'}});
        stack<char> st;
        for (int i = 0; i< s.length(); i++){
            if (s[i] == '(' || s[i] == '{' || s[i] == '[')
                st.push(s[i]);
            else{
                // special case of ']'
                if (st.empty())
                    return false;
                char cur = st.top();
                if (charmap[s[i]] == cur)
                    st.pop();
                else
                    return false;
            }
        }

        if (!st.empty())
            return false;
        return true;
    }
};
