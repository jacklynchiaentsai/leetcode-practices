import heapq
"""
minHeap
time: O(m*n*log(m))
space: O(m*n)
avoid O(log(m*n)) for each minHeap pop -> prioritize top n and store remaining in list
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # create matrrix dist_list[i][j] to store calculations i: worker, j: bike
        dist_list = []
        minHeap = []
        
        for i, worker in enumerate(workers):
            worker_list = []
            
            for j, bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                worker_list.append((dist, i, j))
            
            worker_list.sort(reverse=True) # sorting from largest to smallest distance for popping
            heapq.heappush(minHeap, worker_list.pop())
            dist_list.append(worker_list)
        
        # O(n) for instead of O(m*n)
        heapq.heapify(minHeap)

        answer = [-1] * len(workers)
        bikes_set = set()

        while len(minHeap) > 0:
            dist, worker_idx, bike_idx = heapq.heappop(minHeap)
            if bike_idx in bikes_set:
                # bike is already taken
                heapq.heappush(minHeap, dist_list[worker_idx].pop())
            else:
                if answer[worker_idx] == -1:
                    answer[worker_idx] = bike_idx
                    bikes_set.add(bike_idx)

        return answer
