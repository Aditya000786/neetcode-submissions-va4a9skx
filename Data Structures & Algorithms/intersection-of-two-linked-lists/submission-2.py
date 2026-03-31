class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1, len2 = 0, 0
        curr = headA
        while curr:
           len1+=1
           curr = curr.next

        curr = headB
        while curr:
           len2+=1
           curr = curr.next

        currA, currB = headA, headB
        diff = abs(len1-len2)
        if len1<len2:
            while diff>0:
                currB = currB.next
                diff-=1
        else:
            while diff>0:
                currA = currA.next
                diff-=1

        while currA and currB:
            if currA == currB: return currB
            currA = currA.next
            currB = currB.next
        return None