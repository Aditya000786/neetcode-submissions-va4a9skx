"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}
        old_to_new_map = {}
        curr = head

        while curr:
            new_node = Node(curr.val)
            old_to_new_map[curr] = new_node
            curr = curr.next
        
        dummy = Node(-1)
        prev = dummy
        curr = head
        while curr:
            new_curr = old_to_new_map[curr]
            new_next_curr = old_to_new_map[curr.next] if curr.next else None 
            new_rand_curr = old_to_new_map[curr.random] if curr.random else None 
            new_curr.next = new_next_curr
            new_curr.random = new_rand_curr

            curr = curr.next
            prev.next = new_curr
            prev = new_curr
            # print("pr", prev.value)
        return dummy.next
