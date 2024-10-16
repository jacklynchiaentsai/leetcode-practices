"""
breadth first search
- time: O(m^2 * n^2)
- space: O(m*n)
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isInBound(value, upper_bound):
            if value >=0 and value < upper_bound:
                return True
            else:
                return False
    
        m = len(grid)
        n = len(grid[0])

        minTimeDict = {}
        for row, row_list in enumerate(grid):
            for col, col_val in enumerate(row_list):
                if col_val == 1:
                    minTimeDict[(row, col)] = m*n + 1

        if len(minTimeDict) == 0:
            return 0
        
        for row, row_list in enumerate(grid):
            for col, col_val in enumerate(row_list):
                if col_val == 2:
                    queue = collections.deque([(row, col, 0)])
                    visited = set()
                    while len(queue) > 0:
                        currow, curcol, time = queue.popleft()
                        if (currow, curcol) in minTimeDict:
                            minTimeDict[(currow, curcol)] = min(minTimeDict[(currow, curcol)], time)
                        visited.add((currow, curcol))

                        row_mod = [-1, 0, 1, 0]
                        col_mod = [0, 1, 0, -1]

                        for i in range(len(row_mod)):
                            new_row = currow + row_mod[i]
                            new_col = curcol + col_mod[i]
                            if isInBound(new_row, m) and isInBound(new_col, n):
                                if grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                                    queue.append((new_row, new_col, time+1))

        minMinutes = -1
        print(minTimeDict)
        for row, row_list in enumerate(grid):
            for col, col_val in enumerate(row_list):
                if (row, col) in minTimeDict:
                    curminTime = minTimeDict[(row, col)]
                    if curminTime == m*n + 1:
                        return -1
                    minMinutes = max(minMinutes, curminTime)

        return minMinutes
        

"""
initialize the fresh oranges in graph with minTime m*n + 1
{(row, col): minTime}
when Im on rotten orange perform breadth first search on entire graph every time encounter orange update minTime min(level, minTime)
go through graph again and return the largest minTime

edge cases:
1. if largest minTime = m*n + 1 return -1
2. if there are already no fresh oranges at minute 0 -> 0

2 1 1 2
1 0 1 2
0 1 1 1

minTimeDict = {(0,1): 13, (0,2): 13, (1,0): 13, (1,2): 13, (2,1): 13, (2,2): 13, (2,3): 13}

queue: [(0,1,1), (1,0,1), ]

"""
