"""
two pointer
m = len(slots1)
n = len(slots2)

time: O( mlogm + nlogn)
space: O(1)
"""
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort() 

        slots1_ptr = 0
        slots2_ptr = 0

        # if one pointer goes out of bounds means that no other possible ovelapping intervals
        while slots1_ptr < len(slots1) and slots2_ptr < len(slots2):
            slot1_start, slot1_end = slots1[slots1_ptr]
            slot2_start, slot2_end = slots2[slots2_ptr]

            overlap_start = max(slot1_start, slot2_start)
            overlap_end = min(slot1_end, slot2_end)

            if overlap_end - overlap_start >= duration:
                return [overlap_start, overlap_start + duration]
            else:
                if slot1_end < slot2_end:
                    slots1_ptr += 1
                elif slot2_end < slot1_end:
                    slots2_ptr += 1
                else:
                    slots1_ptr += 1
                    slots2_ptr += 1

        return []
        

"""
two pointer: examine pairs of intervals but update at different rates
which one to update:
    - update one that ends earlier because its next slot might still overlap with the other slot
    - if same end time update both because impossible to move only 1 pointer and have overlap

slots1.sort()
slots2.sort()

slot1_ptr
slot2_ptr

overlap_start = max(slot1.start, slot2,start)
overlap_end = min(slot1.end, slot2.end)

if overlap_end - overlap_start + 1 >= duration
    -> return
else:
    
"""
