/*
inserting nodes in list 1 into list 2
n: length of list1, m: length of list2
time: O(n+m)
space:O(1) -> reusing nodes no extra space created
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
       //need to keep track of previous node as point to insert;
       // initiate as root dummy node
       ListNode* prevnode = new ListNode();
       ListNode* rootnode = prevnode;
       
       // think as picking which node to insert
       while (list1 != nullptr && list2 != nullptr){
           if (list1->val <= list2->val){
               prevnode->next = list1;
               prevnode = prevnode->next;
               list1 = list1->next;
           } else{
               prevnode->next = list2;
               prevnode = prevnode->next;
               list2 = list2->next;
           }
       }

       while(list1!= nullptr){
            prevnode->next = list1;
            prevnode = prevnode->next;
            list1 = list1->next;
       }

       while (list2!= nullptr){
            prevnode->next = list2;
            prevnode = prevnode->next;
            list2 = list2->next;
       }

       return rootnode->next;
    }
};
