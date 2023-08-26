/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        // familiarizing pointers
        ListNode *head = new ListNode(); // create a new list node object
        ListNode *cur = head;

        int carry = 0;
        while (l1 != nullptr && l2 != nullptr){
            // initialize node in beginning so don't create extra node
            ListNode *newNode = new ListNode();
            cur->next  = newNode; 
            cur = cur->next;

            int sum = l1->val + l2->val + carry;
            cur->val = sum % 10;
            if (sum >=10)
                carry = 1;
            else 
                carry = 0;

            l1 = l1->next;
            l2 = l2->next;
        }

        ListNode *temp = nullptr;
        if (l1!= nullptr)
            temp = l1;
        else if (l2!= nullptr)
            temp = l2;

        while (temp != nullptr){
            ListNode *newNode = new ListNode();
            cur->next  = newNode;
            cur = cur->next;

            int sum = temp->val + carry;
            cur->val = sum % 10;
            if (sum >=10)
                carry = 1;
            else 
                carry = 0;

            temp = temp->next;
        }

        if (carry == 1){
            ListNode *newNode = new ListNode(1);
            cur->next  = newNode;
        }

        return head->next;
    }
};
