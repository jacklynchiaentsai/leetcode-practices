/*
graph with breadth first search -> better for finding shortest path
n: number of unique gene strings
time: O(n)
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
        unordered_set<string> genes;
        queue<pair<string, int>> bfs_queue;
        unordered_set<string> visited;
        
        for(string gene: bank){
            genes.insert(gene);
        }

        if (genes.find(endGene) == genes.end()){
            return -1;
        }

        bfs_queue.push({startGene, 0});
        while(!bfs_queue.empty()){
            string curNode = bfs_queue.front().first;
            int mutations = bfs_queue.front().second;
            bfs_queue.pop();
            
            // avoid traversing the same node
            if (visited.find(curNode) != visited.end()){
                continue;
            }

            visited.insert(curNode);

            if (curNode == endGene){
                return mutations;
            }

            // insert all of the strings in bank with 1 length difference
            // this is constant time because char string length 8
            for(int i =0; i< curNode.length(); i++){
                string neighbor = curNode;
                for(char ch: "ACGT"){
                    neighbor[i] = ch;

                    //check if neighbor is in bank
                    if (genes.find(neighbor) != genes.end()){
                        bfs_queue.push({neighbor, mutations + 1});
                    }
                }
            }


        }

        return -1;
    }

    
};

/*
- 8 character string
- A, C, G, T
- corresponding charcter is same -> continue

graph = {gene string: {gene strings that differ by 1 character}}
*/
