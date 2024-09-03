"""
E = Number of edges, V = Number of vertices
time: O(V+E⋅α(n))
space: O(V)
"""
class Solution:
    def getRepresentative(self, node, representative):
        if representative[node] == node:
            return node
        
        return self.getRepresentative(representative[node], representative)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        numConnected = n
        representative = {}

        for i in range(n):
            representative[i] = i

        for edge in edges:
            a = edge[0]
            b = edge[1] 

            a_rep = self.getRepresentative(a, representative)
            b_rep = self.getRepresentative(b, representative)

            if a_rep < b_rep:
                representative[b_rep] = a_rep
                numConnected -= 1
            elif b_rep < a_rep:
                representative[a_rep] = b_rep
                numConnected -= 1

        return numConnected


"""
representative_map = {node: representative}
numConnected
"""
