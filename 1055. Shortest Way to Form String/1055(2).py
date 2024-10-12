"""
2D array memoization of next occuring
source length = m, target length = n
time: O(m + n)
space: O(m) because source can have at most 26 different letters
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        nextidx_dict = {}
        for char in source:
            nextidx_dict[char] = [-1] * len(source)
        

        for i in range(len(source) - 1, -1, -1):
            current_char = source[i]
            if i == len(source) - 1:
                nextidx_dict[current_char][i] = i
                continue
            
            for key, value in nextidx_dict.items():
                if key == current_char:
                    nextidx_dict[key][i] = i
                else:
                    nextidx_dict[key][i] = nextidx_dict[key][i+1]

        print(nextidx_dict)
        num_concat = 1
        source_idx = 0 # keeps track of where we are at source

        for i, target_char in enumerate(target):
            
            if target_char not in nextidx_dict:
                return -1

            if source_idx == len(source) or nextidx_dict[target_char][source_idx] == -1:
                source_idx = 0
                num_concat += 1
            
            source_idx = nextidx_dict[target_char][source_idx] + 1
        
        
        return num_concat



"""
instead of repeatedly iterating through the same source we can just memorize where we should look in source given a character in target

next_idx = {a: []}
"""
