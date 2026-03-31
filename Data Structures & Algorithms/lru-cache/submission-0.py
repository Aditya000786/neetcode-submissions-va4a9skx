from typing import Optional

class Node:
    def __init__(self, key: int, value: Optional[int]):
        self.key = key
        self.value = value
        self.next: Optional[Node] = Node
        self.prev: Optional[Node] = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map:dict[int, Node] = {}
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left

    def update_node_priority(self, node:Node):
        self.evict(node)
        self.insert(node)
        
    def evict(self, node: Node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        
    def insert(self, node: Node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
        # self.left.next.next.prev = self.left
        # self.left.next = self.left.next.next
        # self.right.prev.next = node
        # node.prev = self.right.prev
        # self.right.prev = node
        # node.next = self.right
        a=1
    
    def remove_lru_node(self):
        node_to_remove = self.left.next
        del self.hash_map[node_to_remove.key]
        self.left.next.next.prev = self.left
        self.left.next = self.left.next.next

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.update_node_priority(self.hash_map[key])
            # self.insert_to_right(self.hash_map[key])
            return self.hash_map[key].value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.update_node_priority(self.hash_map[key])
            # self.insert_to_right(self.hash_map[key])
            self.hash_map[key].value = value
        else:
            if len(self.hash_map.keys())>=self.capacity:
                self.remove_lru_node()
            new_node = Node(key, value)
            self.insert(new_node)
            self.hash_map[key] = new_node