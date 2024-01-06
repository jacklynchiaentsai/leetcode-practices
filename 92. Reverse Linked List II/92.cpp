/*
linked list traversal & multiple maps
time: O(n)
space: O(n)
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* curNode = head;
        unordered_map<int, ListNode*> pos_map;
        unordered_map<ListNode*, ListNode*> prev_map;
        int curpos = 1;
        ListNode* prevNode = nullptr;
        
        while(curNode != nullptr){
            pos_map[curpos++] = curNode;
            prev_map[curNode] = prevNode;
            prevNode = curNode;
            curNode = curNode->next;
        }

        if (left == 1 && curpos> 2){
            curNode = pos_map[right];
        } else{
            curNode = head;
        }

        ListNode* newhead = curNode;

        for(int i=1; i < curpos; i++){
            // within reversing range
            if (i >= left && i < right){
                curNode->next = prev_map[curNode];
            } else if (i == left - 1){
                curNode->next = pos_map[right];
            } else{
                if (pos_map.find(i+1) == pos_map.end()){
                    curNode->next = nullptr;
                } else{
                    curNode->next = pos_map[i+1];
                }
            }

            curNode = curNode->next;
        }

        return newhead;
    }
};

/*
pos_map = {int position : ListNOde* correponding node}
prev_map = {ListNode* node: LisNode* previous node in original list}

1->2->3->4->5->6
*/
