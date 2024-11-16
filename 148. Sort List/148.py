# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
top down merge sort
time: O(nlogn)
space: O(logn) -> recursion
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findMiddle(curHead):
            fast_ptr = curHead
            slow_ptr = None

            while fast_ptr and fast_ptr.next:
                fast_ptr = fast_ptr.next.next
                if not slow_ptr:
                    slow_ptr = curHead
                else:
                    slow_ptr = slow_ptr.next
                
            mid = slow_ptr.next
            slow_ptr.next = None
            return mid
        
        def merge(leftHead, rightHead):
            dummyHead = ListNode()
            curNode = dummyHead

            while leftHead and rightHead:
                if leftHead.val < rightHead.val:
                    curNode.next = leftHead
                    leftHead = leftHead.next
                else:
                    curNode.next = rightHead
                    rightHead = rightHead.next

                curNode = curNode.next

            if leftHead:
                curNode.next = leftHead
            else:
                curNode.next = rightHead
            
            return dummyHead.next

        def mergeSort(curHead):
            if curHead == None or curHead.next == None:
                return curHead
            
            # this should be called first because it splits the list
            midNode = findMiddle(curHead)
            lefthead = mergeSort(curHead)
            righthead = mergeSort(midNode)
            return merge(lefthead, righthead)

        if not head:
            return head
        return mergeSort(head)


"""
a b c d
sorting with linked list -> divide and conquer with merge sort (top down)
findMiddle(head){
    fast_ptr = head
    slow_ptr = None -> this is because I want to get the node one step before midpoint to break the linked list
    while fast_ptr hasn't reached the last node:
        move fast_ptr by 2
        move slow_ptr by 1

    mid = slow_ptr.next
    slow_ptr.next = None
    
    return mid
}
merge(left_head, right_head){
    create this dummy head
    while left_head or right_head:
        if left_head is None:
            inserting right_head and updating to next node
        elif right_head is None:
            vice versa
        else:
            we insert the smaller value of either lef_head or right_head
            move the smaller value head to its next
    return dummyHead.next
}
mergeSort(head){
    base case: if head.next == None -> return head
    left_head = mergeSort(head)
    middleNode = findMiddle(head)
    right_head = mergeSort(middleNode)
    return merge(left_head, right_head)
}
"""
