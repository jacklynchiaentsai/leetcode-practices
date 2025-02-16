"""
djikstra's algorithm + skipping processing if traversed through same node earlier in iteration
v = n = number of nodes in graph
e = len(flights) = number of edges in graph
worst case e = v^2
time: O(e*k * log(e*k)) each edge can be at most processed k times
space: O(e + e*k + v) = O(e*k + v)
"""
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}

        for flight in flights:
            sourceNode, destNode, price = flight

            if sourceNode not in graph:
                graph[sourceNode] = {}
            
            graph[sourceNode][destNode] = price

        minHeap = [(0, src, -1)]
        heapq.heapify(minHeap)

        min_stops = {}

        while len(minHeap) > 0:
            curPrice, curNode, curStops = heapq.heappop(minHeap)
            if curNode == dst:
                return curPrice
            
            # if we have already seen curNode with fewer stops, skip processing
            if curNode in min_stops and min_stops[curNode] < curStops:
                continue
            
            min_stops[curNode] = curStops

            # check if curNode has neighbors
            if curNode in graph:
                for neighbor, price in graph[curNode].items():
                    if curStops + 1 <= k:
                        tup = (curPrice + price, neighbor, curStops + 1)
                        heapq.heappush(minHeap, tup)
            
        return -1

"""
from flights create 
graph = {sourceNode: { destNode: price}}

ans
minHeap = [(0, src, -1)]  # [(price, curNode, curStops)]

while minHeap is not empty:
    price, curNode, curStops = popped element of minHeap
    if curNode == dst:
        return price
    
    for neighbor in curNode's neighbors:
        get price2 from curNode to neighbor
        if curStops + 1 <= k:
            update minHeap (price + price2, neighbor, curStops + 1)

return -1
"""
