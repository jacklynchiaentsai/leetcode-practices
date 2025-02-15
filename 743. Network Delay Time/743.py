"""
djikstra's algorithm
n = number of nodes in graph
e = len(times) =  number of edges in the graph
e at most n^2
time: O(eloge) = O(elog(n^2)) = O(elogn)
space: O(e + n)
"""
class Solution:
    import heapq
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for time in times:
            sourceNode, targetNode, time = time
            if sourceNode not in graph:
                graph[sourceNode] = {}
            
            graph[sourceNode][targetNode] = time

        res = None
        seen_set = set()
        minHeap = [(0,k)]
        heapq.heapify(minHeap)
        while len(minHeap) > 0 and len(seen_set) < n:
            time, targetNode = heapq.heappop(minHeap)

            if targetNode not in seen_set:
                if res == None:
                    res = time
                else:
                    res = max(res, time)

                seen_set.add(targetNode)
                
                if targetNode in graph:
                    for neighbor, weight in graph[targetNode].items():
                        heapq.heappush(minHeap, (time + weight, neighbor))

        if len(seen_set) == n:
            return res
        else:
            return -1
     
"""
convert times
graph = {sourceNode: {targetNode: weight}}

res
seen_set = set()
minHeap = [(0, k)] # (time, targetNode)
while minHeap is not empty or seen_set == n:
    # time would be the minimum time it takes from the source node to the targetnode because there are not other exploration paths that are shorter as we are using the minheap

    time, targetnode = pop from minHeap

    # make sure enough time for source node to travel to each of the nodes
    if targetNode not in seen_set:
        res = max(res, time) 
        update seen_set

        for neighbor in targetnode's neighbors:
            add (time + weight, neighbor) to minHeap

return res



"""
