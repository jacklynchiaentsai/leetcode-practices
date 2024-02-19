# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
n: # of nodes in the binary tree
h: binary tree height
time: O(n)
space: O(h) = O(logn)?
"""
class Solution:
    def __init__(self):
        self.sum = 0
    
    def topdowntraversal(self, curNode, curStr):
        curStr += str(curNode.val)
        # leaf node
        if curNode.left == None and curNode.right == None:
            self.sum += int(curStr)
            return None
        
        if curNode.left != None:
            self.topdowntraversal(curNode.left, curStr)
        if curNode.right != None:
            self.topdowntraversal(curNode.right, curStr)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.topdowntraversal(root, "")
        return self.sum

"""
start from root
keep concatenating to string of every layer visited

base case (leaf node):
convert string to number and add to sum

"""
