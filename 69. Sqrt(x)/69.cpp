class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) // cases when x == 0 or 1
            return x;
        // mathematical observation: when x > 2
        // 1 <= sqrt(x) <= x/2 in this rounded down scenario

        // set of integer numbers, pointing to integers rather as indices
        int left = 1, right = x/2;
        while (left <= right){
            int mid = left + (right- left) / 2;
            // avoiding int overflow error
            long int cur_sq = (long)mid*(long)mid;
            long int up_sq = (long)(mid+1) * (long)(mid+1);
            if ( cur_sq <= x &&  up_sq > x)
                return mid;
            else if (cur_sq > x)
                right = mid - 1;
            else
                left = mid + 1;
        }

        // just to avoid error but realistically will never reach here because a square root will definitely exist
        return -1; 
    }
};
