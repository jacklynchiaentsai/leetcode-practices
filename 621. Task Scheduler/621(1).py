"""
maxHeap
tasks length = m 
at most 26 different tasks -> O(1)
time: O(m)
space: O(1)
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
        
        while len(pq_list) > 0:
            cycle = n+1 # cooling period + current task
            tasks_done = 0
            store = []

            while cycle > 0 and len(pq_list) > 0:
                task_num, task = heapq.heappop(pq_list)
                tasks_done += 1 
                task_num += 1
                if task_num < 0:
                    store.append((task_num, task))
                
                cycle -= 1

            for task_tup in store:
                heapq.heappush(pq_list, task_tup)
            
            if len(pq_list) > 0:
                num += n+1
            else:
                num += tasks_done       

        return num        


"""
revision: 
we don't actually need to store the idle tasks just need to update it accordingly in nums

think of cooling periods as cycles

use up the full cycle to perform tasks = tasks_done = n+1, cycle =0
use up full cycle but not enough tasks: tasks_done < n+1, cycle >0
don't need to use up full cycle bc I have no more tasks
"""
