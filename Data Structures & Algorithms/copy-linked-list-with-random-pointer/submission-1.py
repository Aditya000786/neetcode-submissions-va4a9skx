"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# traverse head 
# make a new node 
# establish next link


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        copy_head = Node(head.val)
        random_nodes = []
        curr = head
        curr_copy = copy_head
        hash_map = {curr: curr_copy}
        while curr:
            next_node = curr.next
            copy_next_node = Node(next_node.val) if next_node else None
            curr_copy.next = copy_next_node
            hash_map[next_node] = copy_next_node
            curr = curr.next
            curr_copy = curr_copy.next

        curr = head
        curr_copy = copy_head
        while curr:
            copy_random_node = hash_map[curr.random]
            curr_copy.random = copy_random_node
            curr = curr.next
            curr_copy = curr_copy.next

        return copy_head
        
