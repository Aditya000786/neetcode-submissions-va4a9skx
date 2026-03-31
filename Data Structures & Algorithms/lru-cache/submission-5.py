class Node:
    def __init__(self, key, val = None, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.hash_map = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node

    def remove_from_tail(self):
        node = self.tail.prev
        del self.hash_map[node.key]
        node.prev.next = self.tail
        self.tail.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.move_to_head(node)
            return self.hash_map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value

            node.prev.next = node.next
            node.next.prev = node.prev
            self.move_to_head(node)
        else:
            if self.used == self.capacity:
                self.remove_from_tail()
                self.used-=1

            self.hash_map[key] = Node(key, value)
            self.move_to_head(self.hash_map[key])
            self.used+=1
    
