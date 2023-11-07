// dfs
// time: O(E+V) space: O(E+V) storing adjacency list & recursion stack
class Solution {
public:

    void dfs(int curNode, vector<bool>& visited, vector<vector<int>> adj){
        for(int neighbor: adj[curNode]){
            if (!visited[neighbor]){
                visited[neighbor] = true;
                dfs(neighbor, visited, adj);
            }
        }
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        // adjacency list
        vector<vector<int>> adj(n);
        vector<bool> visited = vector<bool>(n, false);
        int num_connected = 0;

        // constructing the graph
        for(vector<int> edge: edges){
            int node1 = edge[0];
            int node2 = edge[1];

            adj[node1].push_back(node2);
            adj[node2].push_back(node1);
        }

        // dfs
        for (int i = 0; i< n; i++){
            if (!visited[i]){
                dfs(i, visited, adj);
                num_connected++;
            }
        }

        return num_connected;
    }

};
