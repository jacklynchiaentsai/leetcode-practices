class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next  = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addNode(self, node):
        node.next = self.head.next
        node.next.prev = node
        
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            self.removeNode(self.key_to_node[key])
            self.addNode(self.key_to_node[key])
            return self.key_to_node[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.removeNode(self.key_to_node[key])
            self.addNode(self.key_to_node[key])
        
        else:
            node = ListNode(key, value)
            self.key_to_node[key] = node
            self.addNode(node)
        
        if len(self.key_to_node) > self.capacity:
            del_key = self.tail.prev.key
            self.removeNode(self.key_to_node[del_key])
            del self.key_to_node[del_key]





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
key_to_node = {node's key : Node}
head
tail 
"""
