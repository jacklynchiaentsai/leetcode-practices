// BFS
// worst case every element in grid is land -> traversing entire graph
// time: O(m*n) 
// space: O(min(m,n)) maximum length of queue: worst case expanding from middle until hit the sorter end then stop appending to queue
class Solution {
public:
    int dirs[4][2] = {{-1, 0}, {0,1}, {1, 0}, {0, -1}};

    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int totnum = 0;
        vector<vector<bool>> vis(m, vector<bool>(n,false));

        for(int i = 0; i < m; i++){
            for (int j = 0; j< n; j++){
                if (grid[i][j] == '1' && !vis[i][j]){
                    totnum += 1;

                    queue<pair<int, int>> bfs_queue;
                    bfs_queue.push({i, j});

                    while (!bfs_queue.empty()){
                        pair<int, int> curnode = bfs_queue.front();
                        int currow = curnode.first;
                        int curcol = curnode.second;
                        vis[currow][curcol] = true; // mark as visited

                        // traverse through all 4 directions
                        for(int i = 0; i< 4; i++){
                            int newrow = currow + dirs[i][0];
                            int newcol = curcol + dirs[i][1];
                            if (newrow >=0 && newrow <m && newcol>=0 && newcol<n){
                                if (grid[newrow][newcol] == '1' && !vis[newrow][newcol]){
                                    // avoid visiting repeating neighboring nodes
                                    vis[newrow][newcol] = true;
                                    bfs_queue.push({newrow, newcol});
                                }
                            }
                        }
                        bfs_queue.pop();
                    }
                }
            }
        }

        return totnum;
    }
};
