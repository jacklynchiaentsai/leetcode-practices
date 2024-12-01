"""
recursion / backtracking
time: O(n! / k!(n-k)!)
space: O(k)

"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        all_combinations = []

        # with th current comb_list everything I can choose from as the next number would be firstNum all the way up to n
        def getCombinations(comb_list, firstNum):
            if len(comb_list) == k:
                all_combinations.append(comb_list.copy())
                return
            
            # optimizing: no need to explore the next steps if there aren't enough numbers afterwards to fit k
            need = k - len(comb_list)
            remain = n - firstNum + 1
            available = remain - need

            # for each comb_list status have curNum to n numbers to choose from as next number
            for num in range(firstNum, firstNum + available + 1):
                comb_list.append(num)
                # if I had chosen num as my next step then everything I can choose from would be num + 1 to n
                getCombinations(comb_list, num + 1)
                comb_list.pop() # backtracking explore starting with other

        getCombinations([],1)

        return all_combinations
        

"""
9
5
1,2,3,4,5
create numList = [1,2,....n]
for each number choose it or not and I add it up to create list of length k
think of as permutation
    
"""
