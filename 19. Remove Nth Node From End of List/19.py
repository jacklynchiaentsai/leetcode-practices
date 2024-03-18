# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
time: O(N)
space: O(1)
singly linked list traversal, two pointer (fast and slow runner)
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        start = head
        end = head
        
        for _ in range(n):
            end = end.next
            if end == None:
                return head.next
        
        while end.next != None:
            start = start.next
            end = end.next
        
        start.next = start.next.next
        return head


"""
start, end n distance apart
"""
