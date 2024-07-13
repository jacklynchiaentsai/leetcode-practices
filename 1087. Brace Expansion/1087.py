"""
string processing & recursion
N: len(s)
time: O(N * 3^(N/7)) -> complicated math
space: O(N * 3^(N/7))
"""
class Solution:
    def __init__(self):
        self.s_list = []
        self.words_list = []

    def findWords(self, curIndex, curStr):
        if (curIndex >= len(self.s_list)):
            self.words_list.append(curStr)
            return
        
        options = self.s_list[curIndex]
        for letter in options:
            self.findWords(curIndex + 1, curStr + letter)

    def expand(self, s: str) -> List[str]:
        # process input string
        i = 0
        self.s_list = []
        self.words_list = []

        while i < len(s):
            if s[i] == '{':
                j = s.find('}', i)
                parse_string = s[i+1:j]
                self.s_list.append(parse_string.split(','))
                i = j + 1
            else:
                self.s_list.append([s[i]])
                i += 1

        self.findWords(0, "")
        self.words_list.sort()
        return self.words_list
