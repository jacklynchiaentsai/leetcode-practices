// time: O(n) , space: O(1)
// can prove mathematically but all it basically depends on is the direction robot facing after one cycle
class Solution {
public:
    bool isRobotBounded(string instructions) {
        // possible robot movements
        int directions[4][2] ={{0,1}, {1,0}, {0,-1}, {-1,0} };
        // facing north = 0, east = 1, south = 2, west = 3
        int facing = 0;
        int x = 0, y =0;
        for(char instruction:instructions){
            if (instruction == 'G'){
                x += directions[facing][0];
                y += directions[facing][1];
            } else if (instruction == 'L'){
                facing = (facing + 3) % 4;
            } else{
                facing = (facing + 1) % 4;
            }
        }

        // goes back to initial point
        if (x == 0 && y ==0)
            return true;
        
        if (facing != 0)
            return true;
        else
            return false;
    }
};
