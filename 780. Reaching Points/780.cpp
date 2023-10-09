// time: O(log(max(tx,ty))), space: O(1)
// log: think of it as tree alternative choose left and right child each time
// key: working backwards to transform target point to starting point
// constraints: all coordinates >0 -> working backwards is more ideal becauase there is a lower limit
class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        while (tx >= sx && ty >= sy){
            if (tx == ty) // all coordinates >0 -> no moves can be made
                break;
            if (tx>ty && ty>=sy){
                if (ty >sy){
                    // next operation must be (tx-ty, ty) because the other move leads to negative value
                    tx %= ty; 
                }else{ 
                    // ty == sy: satisfied one requirement just need to check other 
                    return (tx-sx) % ty == 0;
                }
            } else{ 
                if (tx > sx){
                    ty %= tx;
                } else{ //tx == sx
                    return (ty-sy) % tx == 0;
                }
            }
        }
        return (tx == sx && ty ==sy);
    }
};
