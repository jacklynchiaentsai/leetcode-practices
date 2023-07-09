class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // convert to set to remove duplicates
        set<int> st(nums.begin(), nums.end());
        vector<int> vc(st.begin(), st.end());
        nums = vc;
        return nums.size();
    }
};
