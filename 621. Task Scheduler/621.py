"""
maxHeap + queue
tasks length = m 
time: O(mn)
space: O(n) -> wait queue
"""
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = {}

        for task in tasks:
            if task not in task_dict:
                task_dict[task] = 0

            task_dict[task] += 1

        pq_list = []
        for key, value in task_dict.items():
            pq_list.append((value * (-1), key))
        
        heapq.heapify(pq_list)

        num = 0
        wait_queue = collections.deque([])
        
        while len(pq_list) > 0 or len(wait_queue) > 0:
            if len(pq_list) > 0:
                task_num, task = heapq.heappop(pq_list)
                task_num += 1


                if len(wait_queue) < n and task_num < 0:
                    while len(wait_queue) < n:
                        wait_queue.append((0,0))
                
                if task_num < 0:
                    wait_queue.append((task_num, task))
            
            num += 1
            if len(wait_queue) > 0:
                task_tup = wait_queue.popleft()
                if task_tup[1] != 0:
                    heapq.heappush(pq_list, task_tup)

        return num        


"""
AAABBCD n = 2
ABCABDA
task_dict = {task: task_num}
[(task_num, task)] -> priority queue
[(0,0), (task_num, task)] -> wait queue

while priority queue is not empty
    - task with largest number remaining
    - place task in wait queue
    - update priority queue with wait queue

note restraints on values (eg: english letters) that can make constant time and space
"""
