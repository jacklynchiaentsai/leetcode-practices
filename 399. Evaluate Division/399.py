"""
adjacency list as nested ditionary + DFS
2N: number of total variables
N: number of equations 
2N: number of edges
m: number of queries
time: O(m* N)
space: O(N)
"""
class Solution:

    def DFS(self, curNode, endNode, adj_list, visited):
        visited.add(curNode)
        if endNode in adj_list[curNode]:
            return adj_list[curNode][endNode]
        
        for neighbor, value in adj_list[curNode].items():
            if neighbor in visited:
                continue
            else:
                div_ans = self.DFS(neighbor, endNode, adj_list, visited)
                if div_ans != -1.0:
                    return value * div_ans

        return -1.0


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = {}
        ans = []
        visited = set()

        for i in range(len(equations)):
            A = equations[i][0]
            B = equations[i][1]
            val = values[i]

            if A not in adj_list:
                adj_list[A] = {}
            
            adj_list[A][B] = val

            if B not in adj_list:
                adj_list[B] = {}
            
            adj_list[B][A] = 1.0 / val
            
        for query in queries:
            start = query[0]
            end = query[1]
            
            if start not in adj_list or end not in adj_list:
                ans.append(-1.0)
            else:
                visited.clear()
                ans.append(self.DFS(start, end, adj_list, visited))
        
        return ans
"""
adj_list = {A: {B: 2.0, C:3.0}}
DFS : visited 
"""
