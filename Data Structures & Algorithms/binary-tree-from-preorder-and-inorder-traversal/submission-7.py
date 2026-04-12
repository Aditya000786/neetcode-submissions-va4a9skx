# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hashmap = {}
        for ind in range(len(inorder)):
            inorder_hashmap[inorder[ind]] = ind
        pre_order_ind = 0

        def dfs(l, r):
            nonlocal pre_order_ind
            if l>r: return None
            root_val = preorder[pre_order_ind]
            pre_order_ind+=1
            root_ind = inorder_hashmap[root_val]
            root_node = TreeNode(root_val)
            root_node.left = dfs(l, root_ind-1)
            root_node.right = dfs(root_ind+1, r)
            return root_node
        return dfs(0, len(inorder)-1)