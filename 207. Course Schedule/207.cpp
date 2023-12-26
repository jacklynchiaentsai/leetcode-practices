/*
topoligical sorting : detecting cycles
time complexity: O(V+E)
- at most, each node will pass in queue
- each edge gets passed once
space complexity: O(V+E) -> adjacency list
*/

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses, 0);
        vector<vector<int>> adj(numCourses);

        //build adjacency list based on edge information: prerequisites
        for(vector<int> prereq: prerequisites){
            int a = prereq[0], b = prereq[1]; // b pointing to a
            adj[b].push_back(a);
            // update indegree
            indegree[a] += 1;
        }

        queue<int> q;
        // initialize queue with nodes of indegree = 0
        for(int i =0; i< numCourses; i++){
            if (indegree[i] == 0){
                q.push(i);
            }
        }

        int nodesvisited = 0; 
        while (!q.empty()){
            int curNode = q.front();
            q.pop();
            nodesvisited++;
            for(int neighbor: adj[curNode]){
                indegree[neighbor]--;
                if (indegree[neighbor] == 0){
                    q.push(neighbor);
                }
            }
        }

        // no more indegree = 0 nodes but haven't visited everything
        return nodesvisited == numCourses;
    }
};
