# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
n: number of nodes
time: O(n)
space: O(n)
- using class attributes as global variables
- topdown tree traversal starts from top but returns bottom up!
- satisfy m out of n true false conditions -> represent as 0,1
"""
class Solution:
    def __init__(self):
        self.pNode = None
        self.qNode = None
        self.ans = None
    
    def topdowntraversal(self, curNode):
        # base case
        if curNode == None:
            return 0
        
        atleft = self.topdowntraversal(curNode.left)
        atright = self.topdowntraversal(curNode.right)
        atnow = 0
        if curNode == self.pNode or curNode == self.qNode:
            atnow = 1
        
        # satisfy two out of 3 true/false conditions
        if atleft + atright + atnow >=2 and self.ans == None:
            self.ans = curNode
        
        return atleft or atright or atnow


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pNode = p
        self.qNode = q
        self.topdowntraversal(root)
        return self.ans


"""
desc_map = {node: set(all descendents of node)}
layer_map = {node: layer}
"""
