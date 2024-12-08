# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
linkedlist
m = len(l1)
n = len(l2)
time: O(max(m,n))
space: O(1)
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Node = l1
        l2Node = l2
        sumHead = ListNode()
        sumNode = sumHead
        carry = 0

        while l1Node != None or l2Node != None:
            if l1Node == None:
                l1val = 0
            else:
                l1val = l1Node.val
                l1Node = l1Node.next

            if l2Node == None:
                l2val = 0
            else:
                l2val = l2Node.val
                l2Node = l2Node.next

            cursum = l1val + l2val + carry
            curval = cursum % 10
            carry = cursum // 10

            curNode = ListNode(val = curval)
            sumNode.next = curNode
            sumNode = sumNode.next

        if carry == 1:
            sumNode.next = ListNode(val = 1)

        return sumHead.next

"""
l1Node
l2Node 
sumHead -> intialize with dummy head node
sumNode = sumHead
carry = 0

while I haven't completely exhausted both list1 and list2:
    get l1val if exists otherwise 0
    same get l2val 

    curval = (l1val + l2val + carry) % 10
    carry = (l1val + l2val + carry) // 10
    

    curNode = ListNode(curval)
    sumNode.next = curNode

    update l1Node, l2Node to next node
    update sumNode to next node

return sumHead.next


"""
