"""
time: O(k log k)
space: O(k)
getting largest or smallest element each time: heapq
keep track of visited element: set
"""
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        pairsHeap = [(nums1[0] + nums2[0], (0,0))] # (sum, (i, j))
        heapq.heapify(pairsHeap)
        visited = set()
        visited.add((0,0))

        while len(ans) < k:
            minsum, (i,j) = heapq.heappop(pairsHeap)
            ans.append([nums1[i], nums2[j]])
            if (i,j+1) not in visited and i < len(nums1) and (j+1) < len(nums2):
                heapq.heappush(pairsHeap, (nums1[i] + nums2[j+1], (i, j+1)))
                visited.add((i,j+1))
            if (i+1, j) not in visited and (i+1) < len(nums1) and j < len(nums2):
                heapq.heappush(pairsHeap, (nums1[i+1] + nums2[j], (i+1, j)))
                visited.add((i+1, j))

        return ans


"""
nums1 size m, nums2 size n
i=0, j=0

i=1, j =0 (smaller) or i=0, j=1

i=1, j=1, 1= 2, j=1
"""
