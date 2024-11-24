# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
multi pointer: linked list in place reversal
time: O(n)
space: O(1)
"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        reverseHead = None
        reverseTail = None
        reverseLeft = None
        reverseRight = None
        newHead = None

        counter = 1
        curNode = head

        while curNode != None:
            if counter == left - 1:
                reverseHead = curNode
            elif counter == right + 1:
                reverseTail = curNode
            elif counter == left:
                reverseLeft = curNode
            elif counter == right:
                reverseRight = curNode
            
            curNode = curNode.next
            counter += 1

        prevNode = reverseLeft
        curNode = reverseLeft.next
        counter = left

        while counter < right:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            counter += 1

        reverseLeft.next = reverseTail
        if reverseHead != None:
            reverseHead.next = reverseRight

        if left > 1:
            return head
        else:
            return reverseRight

        
"""
edge cases:
if left == right -> return Head

first traversal:
reverseHead = node at original left - 1 position
reverseTail = node at original right + 1 position
reverseLeft = node at original left position
reverseRight = node at original right position

second traversal:
prevNode = node at left
curNode = node at left + 1

while prevNode hasn't reached node at right:
    nextNode = curNode.next
    curNode.next = prevNode
    prevNode = curNode
    curNode = nextNode


reverseLeft.next = reverseTail
reverseHead.next = reverseRight

"""
