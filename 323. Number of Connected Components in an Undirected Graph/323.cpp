// disjoint set union
// E = number of edges, V = number of vertices
// time: O(V + E * alpha(n)) space: O(V)
class Solution {
public:
    int findRep(vector<int> representative, int node){
        // the representative's node's representative would always be itself
        if (representative[node] == node){
            return node;
        }

        return findRep(representative, representative[node]);
    }

    int combine(int node1, int node2, vector<int>& connected_size, vector<int>& representative){
        int rep1 = findRep(representative, node1);
        int rep2 = findRep(representative, node2);
        
        // nodes belong in same connected component
        if (rep1 == rep2){
            return 0;
        } else if (connected_size[rep1] > connected_size[rep2]){
            connected_size[rep1] += connected_size[rep2];
            representative[rep2] = rep1;
            return 1;
        } else{
           connected_size[rep2] += connected_size[rep1];
            representative[rep1] = rep2;
            return 1;
        }
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        vector<int> representative(n);
        vector<int> connected_size(n);
        
        // initialization
        for (int i = 0; i < n; i++){
            representative[i] = i;
            connected_size[i] = 1;
        }

        int numconnected = n;
        for(vector<int> edge: edges){
            numconnected -= combine(edge[0], edge[1], connected_size, representative);
        }

        return numconnected;
    }

};
