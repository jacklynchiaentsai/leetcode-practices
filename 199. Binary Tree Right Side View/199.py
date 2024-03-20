from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
breadth first search --> level order traversal
time: O(n)
space: O(n)
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        output = []
        queue = collections.deque([])
        queue.append((root, 1))
        rightNode = root
        layer = 1

        while len(queue) > 0:
            curNode, curlayer = queue.popleft()
            if curlayer != layer:
                output.append(rightNode.val)
                layer = curlayer
            rightNode = curNode

            if curNode.left != None:
                queue.append((curNode.left, curlayer+1))
            if curNode.right != None:
                queue.append((curNode.right, curlayer+1))

        output.append(rightNode.val)
        return output
"""
queue = [(node, layer)]
rightNode
"""
