# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        slow_rev = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow_rev = reverse(slow.next)
        slow.next = None
        list1 = head
        list2 = slow_rev
        dummy = node = ListNode()
        while list1 and list2:
            t_l1 = list1.next
            list1.next = list2
            t_l2 = list2.next
            list1 = t_l1
            list2.next = t_l1
            list2 = t_l2




