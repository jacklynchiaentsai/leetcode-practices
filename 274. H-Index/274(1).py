"""
counting sort
time: O(n)
space: O(n)
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count_list = [0] * ( n + 1 )
        
        # calculate count
        for cit in citations:
            if cit > n:
                count_list[n] += 1
            else:
                count_list[cit] += 1

        cum_count = 0
        for h_cand in range(n, -1, -1):
            cum_count += count_list[h_cand]
            if cum_count >= h_cand:
                return h_cand

"""
k: range of elements
n: len(citations)

trim elements such that k <= n to use counting sort
-> trimming any value > n to n -> does not affect result beacuse h-index upper bound is n

citations = [3,0,6,1,5]
range values 0,1,2,3,4,5 -> this is also h_index
count        1,1,0,1,0,2
num>=        5,4,3,3,2,2

num>= : number of elements >= h_index
"""
