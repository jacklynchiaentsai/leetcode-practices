"""
time: O(1) for all functions
space: O(n) for n elements
"""
from random import choice
class RandomizedSet:

    def __init__(self):
        self.val_dict = {} #val: index in list
        self.val_list = []

    def insert(self, val: int) -> bool:
        if val in self.val_dict:
            return False
        
        self.val_list.append(val)
        self.val_dict[val] = len(self.val_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_dict:
            return False
        
        # swap removing element with last element in list
        remove_idx = self.val_dict[val]
        replace_val =  self.val_list[len(self.val_list) - 1]
        self.val_list[remove_idx] = replace_val
        self.val_dict[replace_val] = remove_idx
        self.val_list.pop()
        del self.val_dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.val_list)
    


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
getRandom: return the head node of linkedlist --> place the head node at the end
node_dict = {val: node}
"""
