"""
matrix traversal: find pattern
n = numRows
m = num of characters in string s
time: O(n * (m / (2n-2) + 1) * (n-1))
space: O(n * (m / (2n-2) + 1) * (n-1))
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        groupnum = 2 * numRows -2
        numCols = (int(len(s) / groupnum) + 1) * (numRows-1)
        matrix = []

        for _ in range(numRows):
            empty_li = [' ' for _ in range(numCols)]
            matrix.append(empty_li)
        
        tracker = numRows - 1
        curr_idx = 0

        for col_idx in range(numCols):
            if tracker == numRows - 1 or tracker ==0:
                for row_idx in range(numRows):
                    matrix[row_idx][col_idx] = s[curr_idx]
                    curr_idx += 1
                    if curr_idx >= len(s):
                        break
                
                if curr_idx >= len(s):
                        break

                if tracker == 0:
                    tracker = numRows - 1
            else:
                matrix[tracker][col_idx] = s[curr_idx]
                curr_idx += 1
                if curr_idx >= len(s):
                    break
            
            tracker -= 1
        
        output_str = ""
        for i in range(numRows):
            for j in range(numCols):
                if matrix[i][j] != ' ':
                    output_str += matrix[i][j]
        
        return output_str
"""
numRows = n
for each n-1 column groups: n+ (n-2)
"""
