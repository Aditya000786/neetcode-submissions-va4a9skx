# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Reaching mid way
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(fast)
        print(slow.val)
        # Reversing after slow pointer
        curr = slow.next
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        slow.next = None


        first = head
        second = prev
        while first and second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next
            second = second_next
            first = first_next
        return None
        

# 0, 6, 1, 5, 2, 4, 3

# 2, 8, 4, 6

# 2, 10, 4, 8, 6f