class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ranges;
        stack<int> st;
        string cur = "";
        for (int i = 0; i< nums.size(); i++){
            if (st.empty()){
                st.push(nums[i]);
            } else if (nums[i] == st.top()+1){
                if (st.size() == 2){
                    st.pop();
                }
                st.push(nums[i]);
            } else{
                if (st.size() == 2){
                    string end = to_string(st.top());
                    st.pop();
                    string start = to_string(st.top());
                    st.pop();
                    cur = start + "->" + end;
                } else{
                    cur = to_string(st.top());
                    st.pop();
                }
                ranges.push_back(cur);
                st.push(nums[i]);
            }
        }

        if (!st.empty()){
            if (st.size() == 2){
                string end = to_string(st.top());
                st.pop();
                string start = to_string(st.top());
                st.pop();
                cur = start + "->" + end;
            } else{
                cur = to_string(st.top());
                st.pop();
            }
            ranges.push_back(cur);
        }

        return ranges;
    }
};
