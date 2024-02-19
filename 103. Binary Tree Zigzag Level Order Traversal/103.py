from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
breadth first search traversal, reverse when right to left
n: total # of nodes binary tree
time: O(n)
space: O(n)
"""
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None:
            return ans
        queue = collections.deque([(root, 1)])
        layer = 1
        layer_li = []
        leftToRight = True

        while len(queue) != 0:
            curNode, curlayer = queue.popleft()
            if curlayer != layer:
                if not leftToRight:
                    layer_li.reverse()
                ans.append(layer_li)
                layer_li = []
                layer = curlayer
                leftToRight = not leftToRight
            
            layer_li.append(curNode.val)
            
            if curNode.left != None:
                queue.append((curNode.left, curlayer+1))
            if curNode.right != None:
                queue.append((curNode.right, curlayer+1))

        if not leftToRight:
            layer_li.reverse()
        ans.append(layer_li)

        return ans
"""
leftToRight = True / False
"""
