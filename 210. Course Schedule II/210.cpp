/*
topological sorting
time: O(V+E)
space: O(V+E)
*/
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses, 0);
        vector<vector<int>> adj(numCourses);
        vector<int> ordering;

        for(vector<int> prequisite: prerequisites){
            int a = prequisite[0];
            int b = prequisite[1];
            // b pointing towards a
            adj[b].push_back(a);
            indegree[a]++;
        }

        queue<int> q;
        for(int i = 0; i < numCourses; i++){
            if (indegree[i] == 0){
                q.push(i);
            }
        }

        while (!q.empty()){
            int curNode = q.front();
            q.pop();
            ordering.push_back(curNode);
            for(int neighbor: adj[curNode]){
                indegree[neighbor]--;
                if (indegree[neighbor] == 0){
                    q.push(neighbor);
                }
            }
        }

        if (ordering.size() == numCourses)
            return ordering;
        else{
            vector<int> emptyarray;
            return emptyarray;
        }
    }
};
