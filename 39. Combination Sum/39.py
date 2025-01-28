"""
bottom up dynamic programming
m = len(candidates) 
n = target
k = max(dp_dict[i])
time: O(m * n * k)
space: O(n * k)
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        
        dp_dict = {}
        for i in range(0, target + 1):
            dp_dict[i] = []
        
        dp_dict[0].append([])

        for candidate in candidates:
            for amount in range(candidate, target + 1):
                new_combinations = []
                for comb in dp_dict[amount - candidate]:
                    new_comb = comb.copy()
                    new_comb.append(candidate)
                    new_combinations.append(new_comb)
            
                dp_dict[amount] = dp_dict[amount] + new_combinations

        return dp_dict[target]

"""
if candidates is empty -> return []

i would range from 0 - target
dp[i]: the number of distinct combination of candidates that can make up the amount i

dp_dict = {amount: [lists of the combinations that make up the amount]}
dp_dict[0] = [[]]
intialize each amount with an empty list []

dp_dict[4] = [2,2]
dp_dict[7] = dp_dict[4] + 3

for candidate in candidates:
    for amount from candidate...target:
        dp_dict[amount] = dp_dict[amount] + 
        appending candidate to every single combination dp_dict[amount - candidate]

dp_dict[target]
"""
