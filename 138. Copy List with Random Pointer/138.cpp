/*
mapping -> hashmap
time: O(N)
space: O(N)
*/

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:

    Node* getNewNode(Node* oldNode, unordered_map<Node*, Node*>& old_new_map){
        if (oldNode == nullptr){
            return nullptr;
        }

        // node doesn't already exist
        if (old_new_map.find(oldNode) == old_new_map.end()){
            old_new_map[oldNode] = new Node(oldNode->val);
        } 

        return old_new_map[oldNode];
    }

    Node* copyRandomList(Node* head) {
        Node* curNode = head;

        unordered_map<Node*, Node*> old_new_map;

        while(curNode != nullptr){
            Node* nextNode = curNode->next;
            Node* randomNode = curNode->random;

            Node* newNode = getNewNode(curNode, old_new_map);
            newNode->next = getNewNode(nextNode, old_new_map);
            newNode->random = getNewNode(randomNode, old_new_map);
            
            curNode = curNode->next;
        }

        return old_new_map[head];
    }
};
