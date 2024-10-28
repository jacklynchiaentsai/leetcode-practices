"""
common prefix -> Trie without isEnd
m: len(arr1)
n: len(arr2)
d: length of longest num
time: O((m+n) * d)
space: O(m*d)
"""
class TrieNode:
    def __init__(self):
        self.children = {} # next_char: TrieNode

class Trie:
    def __init__(self):
        self.rootNode = TrieNode()

    def insert(self, input_str):
        curNode = self.rootNode

        for char in input_str:
            if char not in curNode.children:
                curNode.children[char] = TrieNode()
            
            curNode = curNode.children[char]
    
    def checkPrefix(self, check_str):
        prefix_length = 0
        curNode = self.rootNode
        
        for char in check_str:
            if char not in curNode.children:
                break
            prefix_length += 1

            curNode = curNode.children[char]

        return prefix_length

        

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixtree = Trie()

        for num in arr1:
            prefixtree.insert(str(num))
        
        max_len = 0
        for num in arr2:
            prefix_length = prefixtree.checkPrefix(str(num))
            max_len = max(max_len, prefix_length)

        return max_len
        
"""
intuition: convert to string
only need to find length
brute force -> inefficient
common prefix -> trie!
"""
