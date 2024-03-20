"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
V, E
depth first search
time: O(V+E)
space: O(V+E)
"""
from typing import Optional
class Solution:
    def DFS(self, curNode, old_new_dict, visited):
        if curNode not in old_new_dict:
            newNode = Node(curNode.val)
            old_new_dict[curNode] = newNode
        
        visited.add(curNode)
        
        for neighbor in curNode.neighbors:
            if neighbor not in visited:
                self.DFS(neighbor, old_new_dict, visited)
            
            newNode.neighbors.append(old_new_dict[neighbor])
                

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return node
        old_new_dict = {}
        visited = set()

        self.DFS(node, old_new_dict, visited)
        return old_new_dict[node]
"""
old_new_dict = {oldNode: newNode}
"""
