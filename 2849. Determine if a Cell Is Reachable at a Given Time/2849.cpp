class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        // special case
        if (sx == fx && sy == fy && t == 1)
        return false;
        int maxgap = max(abs(fx-sx), abs(fy-sy));
        return (maxgap > t)? false : true;
    }
};
