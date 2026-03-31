# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        while tail and n>0:
            tail = tail.next
            n-=1
        prev = head
        while tail and tail.next:
            tail = tail.next
            prev = prev.next
        if not tail:
            if head:
                return head.next
            else:
                return head
        while tail.next:
            tail = tail.next
            prev = prev.next
        prev.next = prev.next.next
        return head