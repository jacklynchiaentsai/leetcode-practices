class Solution {
public:
    vector<int> v[100005];
    int longestEqualSubarray(vector<int>& nums, int k) {
        int ans=0;
        for(int i = 0;i<nums.size();i++)v[i].clear();
        for(int i = 0;i<nums.size();i++)v[nums[i]].push_back(i);
        for(int i = 1;i<=nums.size();i++){
            int l=0;
            for(int j=0;j<v[i].size();j++){
                while(v[i][j]-v[i][l]+1-(j-l+1)>k)l++;
                ans=max(ans,(j-l+1));
            }
        }
        return ans;
    }
};
