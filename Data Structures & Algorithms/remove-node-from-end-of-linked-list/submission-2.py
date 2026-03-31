# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        index = 1
        while index <= n:
            start = start.next
            index += 1
        if start is None:
            return head.next
        curr = head
        while start.next:
            start = start.next
            curr = curr.next
        curr.next = curr.next.next
        return head