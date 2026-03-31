class Node:
    def __init__(self, key =-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used_capacity = 0
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def remove_node(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert_at_begin(self, node):
        old_next = self.head.next
        old_next.prev = node
        self.head.next = node

        node.next = old_next
        node.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.map: return -1
        node = self.map[key]
        self.remove_node(node)
        self.insert_at_begin(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)
            self.insert_at_begin(node)
            node.val = value
        else:
            node = Node(key, value)
            self.map[key] = node
            self.insert_at_begin(node)
            self.used_capacity+=1
            if self.used_capacity>self.capacity:
                prev_node = self.tail.prev
                self.remove_node(prev_node)
                del self.map[prev_node.key]
                self.used_capacity-=1



