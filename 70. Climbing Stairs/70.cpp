class Solution {
public:
    int climbStairs(int n) {
        // it is a fibonacci sequence: either climb 1 or 2 steps
        // first calculate the fibonacci sequence
        int fib[45];
        fib[0] = 1;
        fib[1] = 2;
        for(int i = 2; i < n; i++){
            fib[i] = fib[i-2] + fib[i-1];
        }

        return fib[n-1];
    }
};
