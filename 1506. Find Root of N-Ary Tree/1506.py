"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""
"""
key: root of tree is not any node's children
time: O(n)
space: O(n)
"""
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
    
        valNodeMap = {}
        totalSum = 0
        childrenSum = 0

        for node in tree:
            totalSum += node.val
            valNodeMap[node.val] = node

            for children in node.children:
                childrenSum += children.val

        rootVal = totalSum - childrenSum
        
        # alternatively can traverse twice to avoid extra space complexity
        return valNodeMap[rootVal]
