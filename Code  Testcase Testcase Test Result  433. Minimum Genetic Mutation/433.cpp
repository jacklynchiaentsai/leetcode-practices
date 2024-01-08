/*
graph with depth first search
n: number of unique gene strings
time: O(n^2)
space: O(n)
*/
class Solution {
public:
    int chardiff(string gene1, string gene2){
        int count = 0;
        for(int i = 0; i< gene1.length(); i++){
            if (gene1[i] != gene2[i])
                count++; 
        }
        return count;
    }

    int minmutations;

    int minMutation(string startGene, string endGene, vector<string>& bank) {
        unordered_map<string, unordered_set<string>> graph;
        unordered_set<string> genes;
        unordered_set<string> visited; 
        genes.insert(startGene);
        
        for(string gene: bank){
            genes.insert(gene);
        }

        if (genes.find(endGene) == genes.end()){
            return -1;
        }

        if (startGene == endGene){
            return 0;
        }

        vector<string> genes_vec(genes.begin(), genes.end());
        minmutations = genes_vec.size();

        for(int i =0; i< genes_vec.size(); i++){
            for(int j = i+1; j< genes_vec.size(); j++){
                if (chardiff(genes_vec[i], genes_vec[j]) == 1){
                    graph[genes_vec[i]].insert(genes_vec[j]);
                    graph[genes_vec[j]].insert(genes_vec[i]);
                }
            }
        }

        if (DFS(startGene, endGene, graph, visited, 0)){
            return minmutations;
        } else{
            return -1;
        }

    }

    bool DFS(string start, string end, unordered_map<string, unordered_set<string>>& graph, unordered_set<string> visited, int mutations){
        if (graph[start].find(end) != graph[start].end()){
            minmutations = min(minmutations, mutations + 1);
            return true;
        }

        visited.insert(start);

        bool foundpath = false;

        for(string neighbor: graph[start]){
            if (visited.find(neighbor) != visited.end()){
                continue;
            }

            if (DFS(neighbor, end, graph, visited, mutations + 1)){
                foundpath = true;
            }
        }

        return foundpath;
    }
};

/*
- 8 character string
- A, C, G, T
- corresponding charcter is same -> continue

graph = {gene string: {gene strings that differ by 1 character}}
*/
