class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        // using bitwise or property
        vector<int> arr;
        int n = pref.size();
        arr.push_back(pref[0]);

        for(int i = 1; i<n; i++)
            arr.push_back(pref[i]^pref[i-1]);
        return arr;
    }
};
