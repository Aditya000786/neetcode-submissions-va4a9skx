# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        carry = 0
        head = ans

        while l1 and l2:
            n1 = l1.val
            n2 = l2.val
            res = n1 + n2 + carry
            carry = res // 10
            rem = res % 10
            new = ListNode(rem)
            ans.next = new
            ans = ans.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            res = carry + l1.val
            carry = res // 10
            rem = res % 10

            new = ListNode(rem)

            ans.next = new
            ans = ans.next
            l1 = l1.next

        while l2:
            res = carry + l2.val
            carry = res // 10
            rem = res % 10

            new = ListNode(rem)
            ans.next = new
            ans = ans.next
            l2 = l2.next

        while carry:
            new = ListNode(carry)
            ans.next = new
            ans = ans.next
            carry = 0
            
        return head.next