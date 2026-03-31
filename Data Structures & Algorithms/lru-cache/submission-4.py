class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.hash_map = {}
        self.count = 0


    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        
        # Remove from current place
        node = self.hash_map[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        # self
        # print(node.val)

        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        print(key, value)
        if key in self.hash_map:
            # Remove from current place
            node = self.hash_map[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev

            self.head.next.prev = node
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node

        else:
            if self.count>=self.capacity:
                last_node = self.tail.prev
                last_node.prev.next = self.tail
                self.tail.prev = last_node.prev
                self.count-=1
                del self.hash_map[last_node.key]


            node = Node(key, value)
            self.head.next.prev = node
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node
            self.count+=1
            self.hash_map[key] = node
        # print(self.head.next.val)
        # print(self.head.next.next.val)


        
