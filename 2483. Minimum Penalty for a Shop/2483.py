"""
logical reasoning (pattern finding)
time: O(n)
space: O(1)
"""
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        earliesthour = len(customers)
        minpenalty = 0
        Y_count = 0
        N_seen = 0

        for char in customers:
            if char == 'N':
                minpenalty += 1
            else:
                Y_count += 1
        
        for i, char in enumerate(customers):
            curpenalty = Y_count + N_seen
            
            if curpenalty <= minpenalty:
                if curpenalty < minpenalty:
                    earliesthour = i
                else:
                    earliesthour = min(i, earliesthour)

                minpenalty = curpenalty
            
            if char == 'Y':
                Y_count -= 1
            else:
                N_seen += 1

        return earliesthour


"""

earliesthour = n
minpenalty -> calculate accourdingly 
Y_count -> number of Ys in the customers string
N_count = 0
for i, char in customers:
    curpenalty = Y_count + N_seen
    minpenalty = min(minpenalty, curpenalty)
    -> update earliesthour
    if char is Y:
        Y_count -= 1
    else:
        N_count += 1
    

"""
