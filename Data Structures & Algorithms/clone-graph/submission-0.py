from typing import Optional
import collections

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hash_map = {node: Node(node.val)}
        queue = collections.deque([node])
        
        while queue:
            curr_node = queue.popleft()
            for neighbour in curr_node.neighbors:
                if neighbour not in hash_map:
                    hash_map[neighbour] = Node(neighbour.val)
                    queue.append(neighbour)
                hash_map[curr_node].neighbors.append(hash_map[neighbour])
                
        return hash_map[node]
