"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {None: None}
        visited = set()
        def dfs(old_node):
            if old_node in visited or old_node is None:
                return
            if old_node not in old_to_new:
                old_to_new[old_node] = Node(old_node.val)
            new_node = old_to_new[old_node]
            visited.add(old_node)
            for old_neigh in old_node.neighbors:
                if old_neigh not in old_to_new:
                    old_to_new[old_neigh] = Node(old_neigh.val)
                new_node.neighbors.append(old_to_new[old_neigh])
                dfs(old_neigh)
        dfs(node)
        return old_to_new[node]
