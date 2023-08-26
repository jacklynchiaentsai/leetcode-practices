/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {

        // Time complexity: O(2n)

        // special case when list side is 0 or 1
        if (head == nullptr || head->next == nullptr)
            return false;

        ListNode *fast = head->next;
        ListNode *slow = head;

        while(fast != nullptr){
            if (fast == slow)
                return true;
            slow = slow->next;
            if (fast->next == nullptr)
                return false;
            fast = fast->next->next;
        }

        return false;
    }
};
