# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        def merge_2_list(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val <l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail= tail.next
            if l1:
                tail.next=l1
            if l2:
                tail.next=l2
            return dummy.next
        curr_head = lists[0]
        for i in range(1,len(lists)):
            curr_head = merge_2_list(curr_head, lists[i])
        return curr_head