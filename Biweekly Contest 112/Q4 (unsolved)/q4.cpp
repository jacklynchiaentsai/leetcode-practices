class Solution {
public:
    int countKSubsequencesWithMaxBeauty(string s, int K) {
        int n = (int) s.length();
        const int A = 26;
        vector<int> freqs(A, 0);
        for (auto c : s) {
            freqs[c - 'a'] += 1;
        }
        vector<pair<int,char>> P;
        for (int i = 0; i < A; ++i) {
            if (freqs[i] > 0) {
                P.push_back({freqs[i], i});
            }
        }
        
        sort(P.rbegin(), P.rend());
        int sz = (int) P.size();
        if (sz < K) {
            return 0;
        }
        
        const long long MOD = 1'000'000'007;
        long long base = 1;
        int need = K;
        for (int i = 0; i < K; ++i) {
            if (P[i].first > P[K - 1].first) {
                (base *= P[i].first) %= MOD;
                --need;
            }
        }
        int cnt = 0;
        for (int i = 0; i < sz; ++i) {
            if (P[i].first == P[K - 1].first) {
                ++cnt;
            }
        }
        // cout << base << " " << cnt << " " << need << endl;
        long long res = base;
        for (int i = 0; i < need; ++i) {
            (res *= P[K - 1].first) %= MOD; 
        }
        
        vector<long long> invs(A + 1, 1);
        for (int i = 2; i <= A; ++i) {
            invs[i] = MOD - MOD / i * invs[MOD % i] % MOD;
        }
        for (int i = 0; i < need; ++i) {
            (res *= cnt - i) %= MOD;
            (res *= invs[i + 1]) %= MOD;
        }
        return res;
    }
};
