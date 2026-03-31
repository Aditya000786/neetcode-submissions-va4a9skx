from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNode(self, head:ListNode,prev_node: ListNode) -> ListNode:
        if prev_node == None:
            return head.next
        else:
            prev_node.next = prev_node.next.next
            return head
    
    def find_node_number_from_start(self, head: Optional[ListNode], n: int) -> int:
        nodes = 0
        while head:
            head = head.next
            nodes+=1
        return nodes - n
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        n_front = self.find_node_number_from_start(head, n)
        node_to_remove: ListNode = None
        while n_front!=0:
            if node_to_remove==None:
                node_to_remove = head
            else:
                node_to_remove = node_to_remove.next
            n_front -= 1 
        new_head = self.removeNode(head, node_to_remove)
        return new_head