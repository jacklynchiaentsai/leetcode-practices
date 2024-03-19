# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
singly linked list --> determining the nodes we need to access to make the modification
time: O(n)
space: O(1)
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        numNodes = 0
        currNode = head
        lastNode = None
        
        while currNode != None:
            numNodes += 1
            if currNode.next == None:
                lastNode = currNode
            currNode = currNode.next
        
        k = k % numNodes
        visitingNum = numNodes - k - 1

        if k == 0:
            return head
        
        currNode = head
        counter = 0
        while counter < visitingNum:
            counter += 1
            currNode = currNode.next
        
        newHead = currNode.next
        currNode.next = None
        lastNode.next = head

        return newHead


"""
1) determine number nodes n, lastNode
2) determine places to shift
3) determine breaking point 
"""
