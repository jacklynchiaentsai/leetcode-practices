class Solution {
public:
    int dp[100005];
    vector<pair<int,int> > v[100005];
    int maximizeTheProfit(int n, vector<vector<int>>& offers) {
        for(auto it:offers){
            v[it[1]].push_back(make_pair(it[0],it[2]));
        }
        for(int i = 0;i<n;i++){
            if(i!=0)dp[i]=dp[i-1];
            else dp[i]=0;
            for(auto it:v[i]){
                if(it.first==0)dp[i]=max(dp[i],it.second);
                else dp[i]=max(dp[i],it.second+dp[it.first-1]);
            }
        }
        return dp[n-1];
    }
};
