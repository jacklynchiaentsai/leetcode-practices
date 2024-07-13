"""
linked list
- think of edge cases: 0, 1, 1+ nodes, insert in between or at edge
n = number of nodes
time: O(n)
space: O(1)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        insertNode = Node(val = insertVal)

        if head == None:
            insertNode.next = insertNode
            return insertNode

        prevNode = head
        maxNode = head
        first = True

        if prevNode.next == None: # only one node
            head.next = insertNode
            insertNode.next = head.next
            return head


        # insertion scenario : prevNode.val < insertVal and curNode.val >=insertVal
        while prevNode != head or first:
            first = False
            
            if prevNode.val > prevNode.next.val: # the only place that defies non-descending
                maxNode = prevNode
            
            if prevNode.val < insertVal and prevNode.next.val >= insertVal:
                insertNode.next = prevNode.next
                prevNode.next = insertNode
                return head

            prevNode = prevNode.next

        insertNode.next = maxNode.next
        maxNode.next = insertNode

        return head
