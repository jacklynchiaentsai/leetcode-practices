"""
graph + topological sorting 
n: numCourses
m: prerequisites
time: O(n+m)
space: O(n + m)
"""
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = []
        for _ in range(numCourses):
            adjlist.append([])
        
        indegree_map = {}
        for i in range(numCourses):
            indegree_map[i] = 0
        
        ordering = []

        for prereq in prerequisites:
            a = prereq[0]
            b = prereq[1]
            adjlist[b].append(a)
            indegree_map[a] += 1

        queue = collections.deque([])

        for key, value in indegree_map.items():
            if value == 0:
                queue.append(key)

        while len(queue) != 0:
            current = queue.popleft()
            ordering.append(current)
            
            for neighbor in adjlist[current]:
                indegree_map[neighbor] -= 1

                if indegree_map[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(ordering) == numCourses:
            return ordering
        else:
            return []
        
