# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if len(preorder) == 0:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            root_val = preorder[0]
            root_node = TreeNode(root_val)
            root_ind = inorder.index(root_val)
            len_left = root_ind
            root_node.left = dfs(preorder[1:1+len_left], inorder[:root_ind])
            root_node.right = dfs(preorder[1+len_left:], inorder[root_ind+1:])
            return root_node
        return dfs(preorder, inorder)