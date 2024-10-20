"""
stack: iterating forward but updating backwards
time: O(n) : each element at most iterated through twice
space: O(n)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
    
        temp_stack = []
        for i in range(1, len(temperatures)):
            # store the index in which should update
            temp_stack.append((temperatures[i-1], i-1))

            # current temperature shows a rise
            if temperatures[i] > temperatures[i-1]:
                top_temp = temperatures[i]
                cum_days = 1
                
                while len(temp_stack) > 0:
                    cur_temp, cur_index = temp_stack[-1]
                    if cur_temp < top_temp:
                        answer[cur_index] = i - cur_index
                        temp_stack.pop()
                    else:
                        break
        
        return answer
"""
intuition:
for each temp iterate through rest of list until find next_temp larger than temp

inefficiency:
if Im going through a series of declining temperatures then would only need to update it upon temperature rise
- note that the temperature rise might only be larger than a certain group of the declining temperature which would start from the end
--> I want to start checking from the end of the declining temperatures -> last in first out -> stack
"""
