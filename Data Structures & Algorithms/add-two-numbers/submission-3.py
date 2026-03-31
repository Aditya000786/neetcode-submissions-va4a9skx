# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        curr = dummy
        while l1 and l2:
            su = l1.val + l2.val + carry
            carry = su // 10
            rem = su% 10
            curr.next = ListNode(rem)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        l = l1 or l2
        while l:
            temp = l.val + carry
            curr.next = ListNode(temp%10)
            curr = curr.next
            carry = temp // 10
            l = l.next

        while carry:
            curr.next = ListNode(carry)
            carry = 0
            curr = curr.next
        return dummy.next