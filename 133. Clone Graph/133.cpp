/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
/*
breadth first search
N: number of vertices
M: number of edges
time: O(N + M) -> while loop
space: O(N)
*/

class Solution {
public:
    Node* getNewNode(unordered_map<Node*, Node*>& old_new_map, Node* oldNode){
        if (old_new_map.find(oldNode) == old_new_map.end()){
            old_new_map[oldNode] = new Node(oldNode->val);
        }

        return old_new_map[oldNode];
    }

    Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> old_new_map;
        queue<Node* > nodes_queue;
        unordered_set<int> visited;

        if (node == nullptr){
            return nullptr;
        }

        nodes_queue.push(node);
        while (!nodes_queue.empty()){
            Node* curNode = nodes_queue.front();
            nodes_queue.pop();
           
            if (visited.find(curNode->val) != visited.end()){
                continue;
            }

            visited.insert(curNode->val);
            Node* newNode = getNewNode(old_new_map, curNode);
            for (Node* old_neighbor: curNode->neighbors){
                nodes_queue.push(old_neighbor);
                newNode->neighbors.push_back(getNewNode(old_new_map, old_neighbor));
            }
        }

        return old_new_map[node];
    }
};
