class Node{
public:
    int val;

    Node(int nodeval){
        this->val = nodeval;
    }
};
class Solution {
public:
    Node* getNode(unordered_map<int, unordered_map<int, Node*>>& pos_map, int row, int col, vector<vector<int>>& triangle){
        if (pos_map.find(row) == pos_map.end() || pos_map[row].find(col) == pos_map[row].end()){
            pos_map[row][col] = new Node(triangle[row][col]);
        }

        return pos_map[row][col];
    }

    int minpathsum = INT_MAX;
    int minimumTotal(vector<vector<int>>& triangle) {

        if (triangle.size() == 1){
            return triangle[0][0];
        }
        
        unordered_map<Node*, unordered_set<Node*>> graph;
        unordered_map<int, unordered_map<int, Node*>> pos_map;

        for(int i=0; i< triangle.size() -1; i++){
            for(int j =0; j< triangle[i].size(); j++){
                Node* currNode = getNode(pos_map, i, j, triangle);
                Node* neighbor1 = getNode(pos_map, i+1, j, triangle);
                Node* neighbor2 = getNode(pos_map, i+1, j+1, triangle);
                graph[currNode].insert(neighbor1);
                graph[currNode].insert(neighbor2);
            }
        }

        DFS(pos_map[0][0], graph, 0);
        return minpathsum;
    }
    
    void DFS(Node* currNode, unordered_map<Node*, unordered_set<Node*>>& graph, int cursum){
        if (graph.find(currNode) == graph.end()){
            cursum += currNode->val;
            minpathsum = min(minpathsum, cursum);
            return;
        }

        cursum += currNode->val;
        for(Node* neighbor: graph[currNode]){
            DFS(neighbor, graph, cursum);
        }
    }

};

/*
pos_map = {"rownum": {"colnum": Node* of corresponding node at position row, col of triangle}}
*/
