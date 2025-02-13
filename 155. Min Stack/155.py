"""
stack: top element is most recently updated element
time for all functions: O(1)
space: O(n)
"""
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            curMin = self.getMin()
            if val < curMin:
                self.stack.append((val, val))
            else:
                self.stack.append((val, curMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""
(-1, -1),(-2, -2),(-3, -3),(-4, -4),(-3, -4)
init:
initialize empty stack

push:
if stack is empty:
    push (val, val)
else:
    compare val with minimum value of the stack's top element:
    if val is smaller
        push (val, val)
    otherwise
        push (val, top element's min)

pop:
    perform pop operation on stack


"""
