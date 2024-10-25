"""
updating intervals: prefix sum
n: length
m: length of updates
time: O(m + n)
space: O(n)
"""
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length
        update_list = [0] * length

        for update in updates:
            startIdx = update[0]
            endIdx = update[1]
            inc = update[2]

            update_list[startIdx] += inc
            if endIdx + 1 < length:
                update_list[endIdx + 1] -= inc

        cumsum = 0
        for i, value in enumerate(update_list):
            cumsum += value
            arr[i] = cumsum

        return arr
        

"""
arr = [0] * length
update_list = [0] * length

update in updates
startIdx
endIdx
inc

update_list[startIdx] += inc
update_list[endIdx + 1] -= inc
* check if out of range

cumsum = 0
for update_list_val in update_list
    cumsum += update_list_val
    arr[i] = cumsum
"""
