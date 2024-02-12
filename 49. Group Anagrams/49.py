"""
time: O(n * k log k)
space: O(nk)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = {}
        
        for word in strs:
            key = "".join(sorted(word))
            
            if key in anagram_dic:
                anagram_dic[key].append(word)
            else:
                anagram_dic[key] = [word]
        
        ans = []
        for key, value in anagram_dic.items():
            ans.append(value)
        return ans

"""
anagram_dic = {sorted_unique_anagram: [anagram strings]}
k: maximum lenght of str in strs -> sort O(k log k)
n: elemets in strs
"""
