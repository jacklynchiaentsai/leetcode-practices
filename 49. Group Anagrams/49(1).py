"""
dictionary + using word frequency as unique key
n = len(strs)
m = maximum length of all strings in strs
time: O(n*m)
space: O(n*m)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createTuple(input_str):
            freq_list = [0] * 26
            for char in input_str:
                index = ord(char) - ord('a')
                freq_list[index] += 1
            
            return tuple(freq_list)
        
        # (freqa, freqb,...freqz): [word1, word2]
        anagram_dict = {} 

        for input_str in strs:
            anagram_tup = createTuple(input_str)

            if anagram_tup not in anagram_dict:
                anagram_dict[anagram_tup] = []

            anagram_dict[anagram_tup].append(input_str)

        result = []
        for key, anagram_list in anagram_dict.items():
            result.append(anagram_list)

        return result
