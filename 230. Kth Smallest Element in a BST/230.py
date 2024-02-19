import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
n: # of nodes in binary search tree
time: O(n)
space: O(n)
"""
class Solution:
    def __init__(self):
        self.k = -1
    
    def topdowntraversal(self, curNode, pq):
        if len(pq) < self.k:
            heapq.heappush(pq, (-1) * curNode.val)
        else:
            top_ele = pq[0] * (-1)
            if curNode.val < top_ele:
                heapq.heappop(pq)
                heapq.heappush(pq, (-1) * curNode.val)
        
        if curNode.left != None:
            self.topdowntraversal(curNode.left, pq)
        if curNode.right!= None:
            top_ele = pq[0] * (-1)
            if len(pq) < self.k or curNode.right.val < top_ele:
                self.topdowntraversal(curNode.right, pq)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        priority_queue = []
        heapq.heapify(priority_queue)
        self.k = k
        self.topdowntraversal(root, priority_queue)
        return priority_queue[0] * (-1)

"""
priority queue of k elements --> k smallest values ordered from largest to smallest
3,2,1
nodesvisited
traverse left
if nodesvisited >=k
-> don't need to traverse right, end recursion
"""
