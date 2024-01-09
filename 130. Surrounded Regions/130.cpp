/*
mark the connected regions with nodes on borders as E -> escape being flipped
depth first search to mark the entire connected region
m*n = number of cells on the board
time: O(m*n)
space: O(m*n)
*/
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size(), n = board[0].size();
        set<pair<int, int>> visited;
        set<pair<int, int>> bordercells;
        for (int row: {0, m-1}){
            for(int col = 0; col < n; col++){
                bordercells.insert({row,col});
            }
        }

        for (int col: {0, n-1}){
            for(int row = 0; row < m; row++){
                bordercells.insert({row,col});
            }
        }

        for(pair<int, int> cell: bordercells){
            int row = cell.first, col = cell.second;
            if (board[row][col] == 'O')
                DFS(row, col, board, visited);
        }

        for(int i =0; i<m; i++){
            for(int j =0; j<n; j++){
                if (board[i][j] == 'E'){
                    board[i][j] = 'O';
                } else{
                    board[i][j] = 'X';
                }
            }
        }
    }

    void DFS(int row, int col, vector<vector<char>>& board, set<pair<int, int>>& visited){
        visited.insert({row, col});
        vector<int> rowchange = {-1,0,1,0};
        vector<int> colchange = {0,1,0,-1};

        for(int changeindex = 0; changeindex < 4; changeindex++){
            int newrow = row + rowchange[changeindex];
            int newcol = col + colchange[changeindex];

            if (newrow >= 0 && newrow < board.size() && newcol >=0 && newcol < board[0].size()){
                if (visited.find({newrow, newcol}) != visited.end()){
                    continue;
                }
                if (board[newrow][newcol] == 'O'){
                    DFS(newrow, newcol, board, visited);
                }
            }
        }

        board[row][col] = 'E';
    }
};
