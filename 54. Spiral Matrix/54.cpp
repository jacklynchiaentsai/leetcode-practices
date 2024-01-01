/*
matrix traversal pattern
time: O(m*n)
space: O(m*n)
*/
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> ans;
        int row = 0, col = 0;
        int minrow = 0, maxrow = m-1, mincol = 0, maxcol = n-1;
        // 0: right, 1: down, 2: left, 3: up
        int direction = 0;
        while (ans.size() < m*n){
            if (direction == 0){ // right
                while (col <= maxcol){
                    ans.push_back(matrix[row][col]);
                    col++;
                }
                // reset starting point
                col = maxcol;
                row++;
                minrow++; // can no longer visit row
                direction = 1;
            } else if (direction == 2){ // left
                while (col >= mincol){
                    ans.push_back(matrix[row][col]);
                    col--;
                }
                col = mincol;
                row--;
                maxrow--;
                direction = 3;
            } else if (direction == 1){ // down
                while (row <= maxrow){
                    ans.push_back(matrix[row][col]);
                    row++;
                }
                row = maxrow;
                col--; 
                maxcol--;
                direction = 2;
            } else { // up
                while (row >= minrow){
                    ans.push_back(matrix[row][col]);
                    row--;
                }
                row = minrow;
                col++;
                mincol++;
                direction = 0;
            }
        }
        return ans;
    }
};
