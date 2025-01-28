"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
"""
dfs + recursive binary tree preorder traversal
n = number of nodes
time: O(n)
space: O(n) -> imbalanced where nodes are chained with each other only with child pointers
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head

        def dfs(prevNode, curNode):
            if curNode == None:
                return prevNode

            prevNode.next = curNode
            curNode.prev = prevNode

            oldNextNode = curNode.next
            tailNode = dfs(curNode, curNode.child)
            curNode.child = None

            return dfs(tailNode, oldNextNode)
        
        dummyHead = Node(0, None, head, None)
        dfs(dummyHead, head)
        head.prev = None
        return head
"""
edge: 
if head is null return head

def dfs(prevNode, curNode):

    curNode.prev = prevNode
    if curNode.child != None:
        oldnextNode = curNode.next
        curNode.next = curNode.child
        curNode.child = None
        tailNode = dfs(curNode, curNode.next)
        dfs(tailNode, oldnextNode)
    else:
        if curNode.next == None:
            return curNode
        else:
            dfs(curNode, curNode.next)

dummyHead 

dfs(dummyHead, head)
head.prev = None
return head
"""
