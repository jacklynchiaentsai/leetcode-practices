"""
dictionary & matrix traversal
time: O(n^2)
space: O(n^2)
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_dict = {}
        col_dict = {}

        for i, row_list in enumerate(grid):
            tuple_list = tuple(row_list)
            if tuple_list not in row_dict:
                row_dict[tuple_list] = 0

            row_dict[tuple_list]+= 1

        for col in range(n):
            col_list = []
            for row in range(n):
                col_list.append(grid[row][col])
        
            tuple_list = tuple(col_list)
            if tuple_list not in col_dict:
                col_dict[tuple_list] = 0

            col_dict[tuple_list]+= 1

        num = 0
        for tup, count in row_dict.items():
            if tup in col_dict:
                num += count * col_dict[tup]

        return num
            

"""
row_dict = {tup of row_list: count}
col_dict = {tup of col_list: count}

num = 0
for tup, count in row_dict.items():
    num += count * col_dict[tup]
"""
