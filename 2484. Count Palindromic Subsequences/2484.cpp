// multi-dimensional dynammic programming: can make use of multiple arrays to store info
// time: O(100*n) = O(n), space: O(n)
class Solution {
public:
    int countPalindromes(string s) {
        int count[10]; // how many occurence of each digit
        int n = s.length();
        long long int prefix[n][10][10];
        long long int suffix[n][10][10];
        
        memset(count, 0, sizeof(count));
        memset(prefix, 0, sizeof(prefix));
        memset(suffix, 0, sizeof(suffix));

        // updating prefix
        for(int i=0; i<n; i++){
            int digit = s[i] - '0';
            if (i!=0){
                for(int j = 0; j<10; j++){
                    for(int k =0; k<10; k++){
                        prefix[i][j][k] = prefix[i-1][j][k];
                        if (k == digit){
                            prefix[i][j][k] += count[j];
                        }
                    }
                }
            }
            
            count[digit]++;
        }

        memset(count, 0, sizeof(count));

        // updating suffix
        for(int i = n-1; i>=0; i--){
            int digit = s[i] - '0';
            if( i != n-1){
                for(int j =0; j<10; j++){
                    for(int k =0; k<10; k++){
                        suffix[i][j][k] = suffix[i+1][j][k];
                        if(k == digit){
                            suffix[i][j][k] += count[j];
                        }
                    }
                }
            }
            count[digit]++;
        }

        long long int mod = 1e9 + 7;
        long long int ans = 0;
        for(int i = 2; i<n-2; i++){
            for(int j = 0; j<10; j++){
                for(int k = 0; k<10; k++){
                    ans+= prefix[i-1][j][k] * suffix[i+1][j][k];
                    ans = ans % mod;
                }
            }
        }
        return ans;
    }
};
