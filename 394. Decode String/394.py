"""
multi stack problem
maxK = largest repetition number
n = len(s)
time: O(n * maxK)
space: O(n)
"""
class Solution:
    def decodeString(self, s: str) -> str:
        num_st = []
        letter_st = []

        cur_num = ""
        cur_str = ""

        for s_char in s:
            if s_char.isnumeric():
                cur_num += s_char
            
            elif s_char.isalpha():
                cur_str += s_char
            
            elif s_char == '[':
                num_st.append(int(cur_num))
                letter_st.append(cur_str)
                cur_num = ""
                cur_str = ""
            
            elif s_char == ']':
                rep_num = num_st.pop()
                cur_str = letter_st.pop() + rep_num * cur_str
        
        return cur_str

"""
nested -> first in last out -> stack
two different inputs to keep track of -> use different stacks
s = "13[a2[c]]"

num_st = [13, 2]
letter_st = ["", "a"]

cur_num = ""
cur_str = "acc"
for s_char in s:
    if s_char is a digit:
        append to cur_num
    elif s_char is a letter:
        append to cur_str
    elif s_char == '[':
        push cur_num, cur_str to respective stacks
        clear cur_num, cur_str
    else: // encounter ']'
        rep_num = num_st.pop()
        cur_str = letter_st.pop() + rep_num * cur_str

cur_str   
"""
