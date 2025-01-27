"""
recursion + backtracking + dfs
save space with seen_set by changing the marking of current position
k = len(word)
time: O(m*n*(3^k))
space: O(k) -> recursive stack
"""

class Solution:     
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])


        def findword(cur_row, cur_col, cur_index):
            if cur_index == len(word) - 1 and board[cur_row][cur_col] == word[cur_index]:
                return True

            if board[cur_row][cur_col] != word[cur_index]:
                return False
            
            # mark as visited
            board[cur_row][cur_col] = '#'
            row_ch = [0, 1, 0, -1]
            col_ch = [1, 0, -1, 0]

            for i in range(len(row_ch)):
                newrow = cur_row + row_ch[i]
                newcol = cur_col + col_ch[i]

                if newrow >=0 and newrow < m and newcol >=0 and newcol <n:
                    if findword(newrow, newcol, cur_index + 1):
                        return True
            
            # backtracking current step is not feasible
            board[cur_row][cur_col] = word[cur_index]
            return False

        for i in range(m):
            for j in range(n):
                if findword(i, j, 0):
                    return True

        return False
        


            


            
"""
cur_row, cur_col
cur_index of word


"""
