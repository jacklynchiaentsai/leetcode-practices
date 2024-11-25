# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
binary tree: pre-order traversal 
n = number of nodes in binary tree
time: O(n) -> visiting each node once
space: O(n) -> recursive stack
"""

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths = []

        # use list as string is immutable: consuming unecessary space
        def BTTraversal(curNode, path_list):
            path_list.append(str(curNode.val))

            if curNode.left == None and curNode.right == None:
                path_str = '->'.join(path_list)
                all_paths.append(path_str)
            else:
                if curNode.left != None:
                    BTTraversal(curNode.left, path_list)
                
                if curNode.right != None:
                    BTTraversal(curNode.right, path_list)

            path_list.pop() # backtrack to explore other paths

        BTTraversal(root, [])
        return all_paths

"""
all_paths = []
BTTraversal(curNode, path_str):
    append curNode's val into path_str
    if curNode is leaf node:
        append path_str to all_paths
        return
    
    if leftNode is not None:
        BTTraversal(leftNode, path_str)
    do the same for rightNode
"""
        
