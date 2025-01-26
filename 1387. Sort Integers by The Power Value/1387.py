import heapq
"""
recursion + memoization, top k maxHeap
n = hi - lo + 1
collatz conjecture time complexity unknown, assume O(1)
time: O(nlogk)
space: O(k)
"""
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}
        def findPowerVal(num):
            if num in memo:
                return memo[num]
            
            if num % 2 == 0:
                memo[num] = 1 + findPowerVal(num / 2)
            else:
                memo[num] = 1 + findPowerVal(3 * num + 1)

            return memo[num]
        
        maxHeap = []
        heapq.heapify(maxHeap)

        for i in range(lo, hi + 1):
            powerval = findPowerVal(i)

            if len(maxHeap) < k:
                heapq.heappush( maxHeap, (powerval * (-1), i * (-1)))
            else:
                toppower, topval = maxHeap[0]
                toppower *= (-1)
                topval *= (-1)

                if powerval < toppower:
                    heapq.heappop(maxHeap)
                    heapq.heappush( maxHeap, (powerval * (-1), i * (-1)))
                elif powerval == toppower and i < topval:
                    heapq.heappop(maxHeap)
                    heapq.heappush( maxHeap, (powerval * (-1), i * (-1)))

        kthpowerval, kthval = maxHeap[0]
        return kthval * (-1)
"""
def findPowerVal(num)

maxHeap = [(power_val, num_val)] -> maintain size of k

"""
