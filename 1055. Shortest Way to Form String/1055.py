"""
source length = m, target length = n
time: O(mn)
space: O(mn)
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def isSubsequence(string, substr):
            i = 0
            for char in string:
                if char == substr[i]:
                    i += 1
                if i == len(substr):
                    return True
            return False
        
        # handle impossible case
        source_set = set()
        for char in source:
            source_set.add(char)

        for char in target:
            if char not in source_set:
                return -1
        
        # finding number of times
        num_subsequences = 1
        concat_str = source
        while not isSubsequence(concat_str, target):
            concat_str += source
            num_subsequences += 1

        return num_subsequences


"""
intuition:
brute force all subsequences of source
go through target
try to find longest subsequence that exists in source and reomve it

rephrase problem:
because subsequence preserves order of source, can think of it as the number of times I have to concatenate source to have target as one of its subsequences

only -1 if there is any character in target that is not in source

abcd
dcba
"""
