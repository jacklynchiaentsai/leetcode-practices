/*
bottom up greedy: common ascendant pick smaller descendant
N: number of rows in triangle
time: O(N^2)
space: O(1)
*/

class Solution {
public:
    
    int minimumTotal(vector<vector<int>>& triangle) {
        int numrows = triangle.size();
        
        if (triangle.size() == 1){
            return triangle[0][0];
        }

        for(int row = numrows-1; row > 0; row--){
            for(int col = 0; col < triangle[row].size() - 1; col++){
                int child1 = triangle[row][col];
                int child2 = triangle[row][col+1];
                triangle[row-1][col] += min(child1, child2);
            }
        }

        return triangle[0][0];
    }

};
