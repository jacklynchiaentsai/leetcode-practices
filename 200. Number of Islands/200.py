"""
depth first search
time: O(m*n)
space: O(m*n) -> recursive stack
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(cur_row, cur_col):
            if grid[cur_row][cur_col] != '1':
                return

            grid[cur_row][cur_col] = '#'

            row_ch = [0, 1, 0, -1]
            col_ch = [1, 0, -1, 0]

            for i in range(len(row_ch)):
                newrow = cur_row + row_ch[i]
                newcol = cur_col + col_ch[i]

                if newrow >=0 and newrow < m and newcol >=0 and newcol <n:
                    dfs(newrow, newcol)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    num_islands += 1

        return num_islands

"""
num_islands = 0
def dfs(cur_row, cur_col):
    if grid[cur_row][cur_col] is water:
        return

    grid[cur_row][cur_col] = '#'

    visit each neighbor

traverse through each row, col of grid:
    if current cell is land:
        dfs(row, col)
        num_islands += 1
"""
