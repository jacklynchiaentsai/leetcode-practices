# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
two pointer: linkedlist in place traversal
time: O(n)
space: O(1)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        curNode = head

        while curNode != None:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode

        return prevNode
        
"""
2 -> 3
prev  cur

prevNode = None
curNode = head

while curNode != None:
    nextNode = curNode.next
    curNode.next = prev
    prev = curNode
    curNode = nextNode

return prevNode

** adjust the original head's next node to None
"""
