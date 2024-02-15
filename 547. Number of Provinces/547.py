"""
union find
time: O(n^3) --> O(n^2)?
space: O(n)
"""
class Solution:
    def findRep(self, node, rep_map):
        if rep_map[node] == node:
            return node
        
        top_rep = self.findRep(rep_map[node], rep_map)
        rep_map[node] = top_rep
        return top_rep

    def merge(self, node1, node2, rep_map, numcities):
        rep1 = self.findRep(node1, rep_map)
        rep2 = self.findRep(node2, rep_map)

        if rep1 == rep2:
            return 0
        else:
            if numcities[rep1] >= numcities[rep2]:
                rep_map[rep2] = rep1
                numcities[rep1] += numcities[rep2]
            else:
                rep_map[rep1] = rep2
                numcities[rep2] += numcities[rep1]
            return 1


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = n

        rep_map = {}
        numcities = {}

        for i in range(n):
            rep_map[i] = i
            numcities[i] = 1
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    provinces -= self.merge(i, j, rep_map, numcities)

        return provinces
        

"""
graph
union find
"""
