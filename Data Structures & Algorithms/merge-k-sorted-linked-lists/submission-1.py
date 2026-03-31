# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node_set = False
        min_value = float('infinity')
        res = ListNode()
        head = res
        while True:
            for i in range(len(lists)):
                curr = lists[i]
                # print("curr", curr, i)
                if curr and curr.val < min_value:
                    # print("i", i)
                    node_set = True
                    min_node_ind = i
                    min_value = curr.val
            
            if not node_set:
                return head.next
            res.next = lists[min_node_ind]
            res = res.next
            # print("min_node_ind",min_node_ind)
            # print("lists[min_node_ind]", lists[min_node_ind], lists[min_node_ind].val)
            lists[min_node_ind] = lists[min_node_ind].next
            min_value = float('infinity')
            node_set = False