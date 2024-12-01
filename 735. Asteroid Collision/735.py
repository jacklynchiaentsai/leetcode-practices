"""
stack: evaluating previous elements from closest to furthest
time: O(n) -> each asteroid is at most processed twice
space: O(n)
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        surviving_st = []
        for asteroid in asteroids:
            if len(surviving_st) == 0:
                surviving_st.append(asteroid)
            else:
                top_ele = surviving_st[-1]
                # consider that if the asteroids are flying in opposite directions they won't collide
                if asteroid * top_ele > 0 or (top_ele < 0 and asteroid > 0):
                    surviving_st.append(asteroid)
                else:
                    surviving_wins = True
                    while len(surviving_st) > 0:
                        top_ele = surviving_st[-1]

                        # consider the case of same sign: no collision
                        if top_ele * asteroid > 0:
                            break
                        if abs(top_ele) > abs(asteroid):
                            surviving_wins = False
                            break
                        elif abs(top_ele) == abs(asteroid):
                            surviving_st.pop()
                            surviving_wins = False
                            break
                        else:
                            surviving_st.pop()

                    if surviving_wins:
                        surviving_st.append(asteroid)

        return surviving_st


""" 
st = [] -> surviving asteroids
iterating forwards but updating 

"""
