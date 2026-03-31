class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while True:
            min_node = ListNode(float('inf'))
            min_ind = -1
            for i in range(len(lists)):
                li = lists[i]
                if li:
                    if li.val<min_node.val:
                        min_node = li
                        min_ind = i
            if min_ind == -1:
                return dummy.next
            else:
                curr.next = min_node
                curr = curr.next
                lists[min_ind] = lists[min_ind].next
        
