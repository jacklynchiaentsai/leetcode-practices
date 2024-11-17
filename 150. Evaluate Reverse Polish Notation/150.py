"""
stack (last in first out)
time: O(n)
space: O(n)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op_set = set(['+', '-', '*', '/'])
        for token in tokens:
            if token in op_set:
                num2 = st.pop()
                num1 = st.pop()
                
                if token == '+':
                    st.append(num1 + num2)
                elif token == '-':
                    st.append(num1 - num2)
                elif token == '*':
                    st.append(num1 * num2)
                else:
                    st.append(int(num1 / num2))
            else:
                num = int(token)
                st.append(num)

        return st[-1]
"""
st = [] # numbers to be used in operation
for token in tokens:
    if token is an operator:
        pop num1, num2 from stack
        perform operation on num1 num2 -> result
        push result into stack
    else:
        push num into stack

    return top of stack
"""
