class Solution {
public:

    // O(nlog(n))
    bool isValidSudoku(vector<vector<char>>& board) {
        set< pair<int, char>> rowset, colset, gridset;

        char ele;
        int gridnum;

        for(int i=0; i<9; i++){
            for(int j = 0; j<9; j++){
                ele = board[i][j];

                if (ele == '.')
                    continue;
                
                // generate unique grid num
                gridnum = (i/3) *3 + (j/3);

                pair <int, char>p;
                p.first = i;
                p.second = ele;

                // row check
                if (rowset.find(p) == rowset.end()){
                    rowset.insert(p);
                } else{
                    return false;
                }

                // col check
                p.first = j;
                if (colset.find(p) == colset.end()){
                    colset.insert(p);
                } else{
                    return false;
                }

                // grid check
                p.first = gridnum;
                if (gridset.find(p) == gridset.end()){
                    gridset.insert(p);
                } else{
                    return false;
                }

            }
        }

        return true;
    }   
};
