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
bottom up recursion
time: O(n^2) -> all cells in grid will be called exactly once
space: O(logn) -> recursive depth
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def constructQuad(rowl, rowh, coll, colh):
            if (rowh - rowl) == 1 and (colh - coll) == 1:
                nodeval = grid[rowl][coll]
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

                if rootNode.topLeft.isLeaf and rootNode.topRight.isLeaf and rootNode.bottomLeft.isLeaf and rootNode.bottomRight.isLeaf:
                    if rootNode.topLeft.val == rootNode.topRight.val and rootNode.topRight.val == rootNode.bottomLeft.val and rootNode.bottomLeft.val == rootNode.bottomRight.val:
                        rootNode = Node(rootNode.topLeft.val, True, None, None, None, None)
                return rootNode

        n = len(grid)
        return constructQuad(0, n, 0, n)

"""
top down solution has redudancy of running isAllSame on the same cells in grid multiple times
-> optimizing with bottom strategy where we narrow it down to the smallest space and build up the tree

constructQuad(rowl, rowh, coll, colh):
    if inspecting only one grid cell:
        create leaf node for it

    else:
        construct empty rootNode with isLeaf as False
        rootNode.topLeft = constructQuad(rowl, midrow, coll, midcol)
        rootNode.topRight = constructQuad(rowl, midrow, midcol, colh)
        rootNode.bottomLeft = constructQuad(midrow, rowh, coll, midcol)
        rootNode.bottomRight = constructQuad(midrow, rowh, midcol, colh)

        if the values of the 4 nodes are the same and the 4 nodes are leaf:
            reset rootNode to be a leaf node with the shared value

        return rootNode
"""
