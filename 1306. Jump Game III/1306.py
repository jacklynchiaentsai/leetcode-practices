"""
breadth first search
n = len(arr)
time: O(n)
space: O(n)
"""
import collections
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = collections.deque([start])
        visited = set()

        def isInRange(index):
            if index >=0 and index < len(arr):
                return True
            return False
        
        def updateQueue(index):
            if isInRange(index) and index not in visited:
                queue.append(index)
        
        while len(queue) > 0:
            i = queue.popleft()
            visited.add(i)

            if arr[i] == 0:
                return True

            updateQueue(i+arr[i])
            updateQueue(i - arr[i])

        return False
            
"""
breadth first search
queue = [start] # stores index to visit
visited = set() # stores index visited

while queue is not empty:
    i = top element of queue
    check if it is index with value 0 -> return true
    if not then put i + arr[i], i - arr[i] into queue if within range of arr

return false
""" 
