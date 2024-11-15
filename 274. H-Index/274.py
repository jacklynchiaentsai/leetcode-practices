"""
reverse sorting + mathematical inference
time: O(nlogn)
space: O(1)
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        found = False
        h_index = 0

        for i in range(0, len(citations)):
            if citations[i] > i:
                h_index = i+1
            
        return h_index
"""
sorting: order doesn't matter, finding max want to validate from the smallest possible h-index to see what's the largest possible h-index I can achieve

1. observation h_index range [0, len(citations)]
2. sort in descending order
- if citations[i] > i -> papers 0~i have num of citations >= i + 1
    i.o.w. I have i+1 papers where num of citations >= i+1 -> h_index definition
- else:
    I don't have enough papers to support the i+1 h_index
"""
