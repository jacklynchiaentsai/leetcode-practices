# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
depth first search
n = number of nodes in binary tree
time: O(n^2)
-> worst case complete binary tree with N/2 leaves
-> for every leaf copy operation takes O(n)
space: O(n)
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []

        all_paths = []
        def dfs(curNode, curSum, curPath):
            curSum += curNode.val
            curPath.append(curNode.val)

            if curNode.left == None and curNode.right == None:
                if curSum == targetSum:
                    all_paths.append(curPath.copy())
                curPath.pop()
                return

            if curNode.left != None:
                dfs(curNode.left, curSum, curPath)

            if curNode.right != None:
                dfs(curNode.right, curSum, curPath)

            curPath.pop()

        dfs(root, 0, [])
        return all_paths
            

"""
edge case: root = None -> return []

all_paths = []
depth first search: root-to-leaf paths
dfs(curNode, curSum, curPath):
    curSum += curNode.val
    add curNode.val to curPath

    if curNode is a leafNode:
        if curSum == targetSum:
            add curPath to all_paths
        curPath.pop()
        return

    if lefNode is not None:
        dfs(curNode.left, curSum, curPath)
    
    do the same for rightNode
    curPath.pop() -> backtracking

"""
