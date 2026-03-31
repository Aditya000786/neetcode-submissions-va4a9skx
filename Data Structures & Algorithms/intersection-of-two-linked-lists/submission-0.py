class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = {}
        curr = headA
        while curr:
            visited[curr] = curr
            curr = curr.next
        curr = headB
        while curr:
            if curr in visited: return curr
            curr = curr.next
        return None