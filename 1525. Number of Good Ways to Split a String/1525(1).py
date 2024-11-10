"""
use dictionary and set to count character frequency
time: O(n) -> note that single traversal
space: O(1)
"""

class Solution:
    def numSplits(self, s: str) -> int:
        # at most 26 characters
        first_dict = {}
        last_dict = {}

        for i, char in enumerate(s):
            if char not in first_dict:
                first_dict[char] = i
            last_dict[char] = i

        indices = list(first_dict.values()) + list(last_dict.values())
        indices.sort()

        middle = len(indices) // 2
        return indices[middle] - indices[middle -1]


"""
solution: https://leetcode.com/problems/number-of-good-ways-to-split-a-string/solutions/1520004/99-7-python-3-solution-with-17-lines-no-search-explained/
smart approach: reducing space complexity + single iteration
intuition: given a split to determine if each side has a certain character, keep track of first occuring index and last occuring index
first = {char: first occuring index}
last = {char: last occuring index}

take first.values and last.values and I sort them into list indices
-> the middle area woulkd be where the number of distinct characters are balanced
-> reasoning if first on the left side then last index of the same character can either be on left or on right side
-> if on right side -> this character is balanced on both sides
-> if on left side -> given that both sides have the same size, we know that on the right side there must also be a first and last of a different character -> number of distinct characters are still balanced

we have calculate the size of this middle area
because len(indices) is even this would be indices[middle] - indices[middle - 1]

0,1,3,5
"""
