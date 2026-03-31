# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        start = head
        prev_tail = ListNode(-1)
        dummy = prev_tail
        while True:
            curr = start
            i = k-1

            while curr and i>0:
                curr = curr.next
                i-=1
            if not curr:
                prev_tail.next = start
                break

            next_head = curr.next
            curr.next = None
            new_head = reverse(start)

            prev_tail.next = new_head
            prev_tail = start

            start = next_head

        return dummy.next



