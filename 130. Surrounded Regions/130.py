"""
depth first search on 2D matrix, only traversing based on criteria
time: O(m*n)
space: O(m*n)
"""
class Solution:

    def DFS(self, row, col, board, visited):
        # need to mark visited 
        if board[row][col] == 'O':
            board[row][col] = 'Y'
        else:
            return None
        
        visited.add((row, col))

        row_change = [-1, 0, 1, 0]
        col_change = [0, 1, 0, -1]

        for i in range(len(row_change)):
            newrow = row + row_change[i]
            newcol = col + col_change[i]
            if newrow >=0 and newrow < len(board) and newcol >=0 and newcol < len(board[0]):
                if (newrow, newcol) not in visited:
                    self.DFS(newrow, newcol, board, visited)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        visited = set()

        for row in [0, m-1]:
            for col in range(n):
                if board[row][col] == 'O':
                    print((row, col))
                    self.DFS(row, col, board, visited)
        
        for col in [0, n-1]:
            for row in range(1, m-1):
                if board[row][col] == 'O':
                   self.DFS(row, col, board, visited)

        print(board)
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'Y':
                    board[row][col] = 'O'
        
