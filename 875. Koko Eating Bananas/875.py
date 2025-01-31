"""
binary search
n = len(piles)
m = max(piles)
time: O(logm * n)
space: O(1)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 0:
            return 0

        left ,right = 1, max(piles)
        while left < right:
            med = left + (right- left) // 2

            numhours = 0
            for pile in piles:
                numhours += math.ceil(pile / med)

            if numhours <= h:
                right = med
            else:
                left = med + 1

        return right
            

"""
lowest k value 0
highest k value max(piles)


0..... max(piles)
if koko can finish in kmin then can also finish in kmin + 1
if koko can't finish in kmin then also can't also finish in kmin - 1

piles = [3,6,7,11], h = 8
0 ..4.5 11

left = 0, right = len(piles) - 1

while left < right:
    med

    if koko is able to finish piles at med speed:
        right = med
    else:
        left = med + 1

return right

"""
