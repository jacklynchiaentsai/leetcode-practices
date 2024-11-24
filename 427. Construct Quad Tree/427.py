"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
"""
recursion
time: O(n^2* logn)
space: O(logn) -> recursive stack
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def isAllSame(rowl, rowh, coll, colh):
            firstVal = grid[rowl][coll]
            for i in range(rowl, rowh):
                for j in range(coll, colh):
                    if grid[i][j] != firstVal:
                        return -1
            
            return firstVal

        def constructQuad(rowl, rowh, coll, colh):
            allsame = isAllSame(rowl, rowh, coll, colh)
            if allsame != -1:
                nodeval = True if allsame == 1 else False
                leafNode = Node(nodeval, True, None, None, None, None)
                return leafNode
            
            else:
                rootNode = Node(True, False, None, None, None, None)
                midrow = rowl + (rowh - rowl) // 2
                midcol = coll + (colh - coll) // 2
                rootNode.topLeft = constructQuad(rowl, midrow, coll, midcol)
                rootNode.topRight = constructQuad(rowl, midrow, midcol, colh)
                rootNode.bottomLeft = constructQuad(midrow, rowh, coll, midcol)
                rootNode.bottomRight = constructQuad(midrow, rowh, midcol, colh)
                return rootNode

        n = len(grid)
        return constructQuad(0, n, 0, n)

"""

def isAllSame():
    save value of first node
    go through remaining nodes
        if node value different from first node -> -1
    return 1 or 0 depending on the value of the first node

constructQuad(rowl, rowh, coll, colh):
    if isAllSame():
        construct leaf node of the corresponding same value and return it

    else:
        construct empty rootNode with isLeaf = False
        rootNode.topLeft = constructQuad(rowl, rowh / 2, coll, colh / 2)
        rootNode.topRight = constructQuad(rowl, rowh / 2, colh / 2, colh)
        rootNode.bottomLeft = constructQuad(rowh / 2, rowh, coll, colh / 2)
        rootNode.bottomRight = constructQuad(rowh / 2, rowh, colh / 2, colh)

constructQuad(0, n, 0, n)
"""
