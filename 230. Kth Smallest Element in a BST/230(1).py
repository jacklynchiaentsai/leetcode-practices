# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
binary search tree: in order traversal
H: height of binary search tree -> n in worst case skewed BST and log(n) for average case balanced BST
time: O(H+k) = O(n)
-> H for the deepest we would go down the BST before hitting a leaf node 
-> k for visiting k nodes as we recurse back up
space: O(H) = O(n)
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes_visited = 0
        kthsmallest = None

        def BSTTraversal(curNode):
            nonlocal nodes_visited, kthsmallest

            if curNode.left != None:
                BSTTraversal(curNode.left)
            
            nodes_visited += 1
            if nodes_visited == k:
                kthsmallest = curNode.val
                return
            
            if curNode.right != None:
                BSTTraversal(curNode.right)

            return

        BSTTraversal(root)
        return kthsmallest

"""
traverse binary search tree in order from smallest to largest 
-> upon visiting the kth node I can return it

-> in-order traversal of BST
nodes_visited = 0
kthsmallest = None

BSTTraversal(curNode):
    if leftnode is not None:
        BSTTraversal(leftnode)
    
    nodes_visited += 1

    if nodes_visited == k:
        kthsmallest = curNode.val
        return

    if rightnode is not None:
        BSTTraversal(rightnode)

    return

    
    
"""
