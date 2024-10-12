"""
two pointer + greedy
source length = m, target length = n
time: O(m*n)
space: O(m)
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        # handle impossible case
        source_set = set()
        for char in source:
            source_set.add(char)

        for char in target:
            if char not in source_set:
                return -1
        
        target_idx = 0
        source_idx = 0
        num_concat = 0

        while target_idx < len(target):
            if source_idx == len(source):
                num_concat += 1
                source_idx = 0
            
            if target[target_idx] == source[source_idx]:
                target_idx += 1

            source_idx += 1

        # taking into account the last iteration of source
        num_concat += 1

        return num_concat


"""
intuition:
don't waste space with concatenation or time with finding subsequence since we're just looping through source string
"""
