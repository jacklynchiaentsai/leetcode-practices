# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
binary tree: post order traversal
consider all possible paths that can formed given curNode and children
time: O(n)
space: O(n)
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpathsum = root.val

        def BTTraversal(curNode):
            nonlocal maxpathsum

            # single node can form maximum path sum on its own
            singularnodesum = curNode.val
            maxpathsum = max(maxpathsum, singularnodesum)

            if curNode.left == None and curNode.right == None:
                return curNode.val

            leftVal = 0
            rightVal = 0

            if curNode.left != None:
                leftVal = BTTraversal(curNode.left)

            if curNode.right != None:
                rightVal = BTTraversal(curNode.right)

            bothpathsum = leftVal + curNode.val + rightVal
            singlepathsum = curNode.val + max(leftVal, rightVal)

            maxpathsum = max(maxpathsum, bothpathsum)
            maxpathsum = max(maxpathsum, singlepathsum)

            return max(singlepathsum, singularnodesum)

        BTTraversal(root)

        return maxpathsum
            
"""
observation: 
- traverse binary tree: post-order traversal -> as leaf nodes only have single possible path so should consider those first
- recursive iteration: return singular path all the way up from bottom of tree to curNode
    - base case: leaf node -> maximum path sum would be itself


- given root node and two child nodes -> 2 potential ways I can form maximum path sum
- if decide to take the paths of both its leaf nodes 
    -> finalized maximum path sum
- else: take the child path with the larger maximum path sum and continue recursing upwards to see if I can form a larger maximum path

global variable maxpathsum

BTTraversal(curNode):
if curNode is leaf node:
    retuurn curNode.val

if leftNode is not None:
    leftval = BTTraversal(leftNode)

do the same for the rightNode -> store in rightval

bothpathsum = leftval + curNode.val + rightval
singlepathsum = curNode.val + max(leftval, rightval)
maxpathsum = max(maxpathsum, bothpathsum)
maxpathsum = max(maxpathsum, singlepathsum)

return singlepathsum -> because I can only pick one 


"""
