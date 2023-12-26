/*
depth first search: detecting cycles -> check if element is in recursion stack
time complexity: O(V+E) -> at most visit each vertice and edge once
space complexity: O(V+E)
*/

class Solution {
public:

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<bool> visited(numCourses, false);
        // used to check if node is in recursion stack -> cycle detection
        vector<bool> instack(numCourses, false);

        //build adjacency list based on edge information: prerequisites
        for(vector<int> prereq: prerequisites){
            int a = prereq[0], b = prereq[1]; // b pointing to a
            adj[b].push_back(a);
        }
        
        // explore every node as a starting point
        for(int i =0; i< numCourses; i++){
            if (dfs(i, adj, visited, instack)){
                return false;
            }
        }
        return true; 
    }  

    // returns true if detects cycle
    bool dfs(int curNode, vector<vector<int>>& adj, vector<bool>& visited, vector<bool>& instack){
        // base cases
        // check if cycle exists
        if (instack[curNode]){
            return true;
        }
        // already visited and not part of cycle
        if (visited[curNode]){
            return false;
        }

        // mark as visited
        visited[curNode] = true;
        // curNode is ancestor of all neighboring nodes so will be in their recursion stack
        instack[curNode] = true; 
        for(int neighbor: adj[curNode]){
            if (dfs(neighbor, adj, visited, instack))
                return true;
        }
        instack[curNode] = false;
        return false;
    }
};
