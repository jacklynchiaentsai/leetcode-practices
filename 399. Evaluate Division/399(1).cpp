/*
- graph with weights using nested hashmap
- depth first search with memoization

n: number of equations
m: number of queries

time: O(mn)
space: O(n)
*/

class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        vector<double> responses;
        // adjacency list for graph with weights
        unordered_map<string, unordered_map<string, double> > eq_graph;
        unordered_set<string> var_set;
        unordered_set<string> visited;

        // constructing graph form equation relationships
        for(int i = 0; i< equations.size(); i++){
            vector<string> eq_pair = equations[i];
            double value = values[i];
            string first = eq_pair[0];
            string second = eq_pair[1];

            eq_graph[first][second] = value;
            eq_graph[second][first] = 1/value;

            var_set.insert(first);
            var_set.insert(second);
        }

        for(vector<string> query: queries){
            string start = query[0];
            string end = query[1];

            if (var_set.find(start) == var_set.end() || var_set.find(end) == var_set.end()){
                responses.push_back(-1.0);
                continue;
            }

            visited.clear();
            responses.push_back(DFS(start, end, eq_graph, visited));

        }
        return responses;
    }

    double DFS(string start, string end, unordered_map<string, unordered_map<string, double> >& eq_graph, unordered_set<string>& visited){
        if (eq_graph.find(start) != eq_graph.end() && eq_graph[start].find(end) != eq_graph[start].end()){
            return eq_graph[start][end];
        }

        visited.insert(start);

        for(auto it: eq_graph[start]){
            string key = it.first;
            double val = it.second;

            if (visited.find(key) != visited.end()){
                continue;
            }

            double inter_val = DFS(key, end, eq_graph, visited);

            if (inter_val != -1.0){
                eq_graph[start][end] = val * inter_val;
                return eq_graph[start][end];
            }
            
        }

        return -1.0;
    }
};

/*
graph  ={ "a" : {"b": 2.0, "c": 3.0}}

*/
