/*
merge sort strategy
n: length of list1, m: length of list2
time: O(n+m)
space:O(n+m) -> extra space when creating new merged list
*/
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // dummy root node
        ListNode* curNode = new ListNode();
        // keep record
        ListNode* rootNode = curNode;

        bool isfirst = true;
        while (list1 != nullptr && list2 != nullptr){
            int minval;
            if (list1->val <= list2->val){
                minval = list1->val;
                list1 = list1->next;
            }else{
                minval = list2->val;
                list2 = list2->next;
            }

            curNode->next = new ListNode(minval);
            curNode = curNode->next;
        }

        // remaining nodes in list1
        while(list1!= nullptr){
            curNode->next = new ListNode(list1->val);
            curNode = curNode->next;
            list1 = list1->next;
        }

        // remaining nodes in list2
        while(list2!= nullptr){
            curNode->next = new ListNode(list2->val);
            curNode = curNode->next;
            list2 = list2->next;
        }

        return rootNode->next;
    }
};
