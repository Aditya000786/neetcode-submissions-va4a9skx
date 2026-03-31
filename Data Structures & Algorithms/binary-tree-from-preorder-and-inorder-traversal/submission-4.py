# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if len(inorder)<=0: return None
            root_val = preorder[0]
            root = TreeNode(root_val)
            mid = inorder.index(root_val)
            root.left = dfs(preorder[1: 2+mid], inorder[:mid])
            root.right = dfs(preorder[1+mid:], inorder[mid+1:])
            return root
        return dfs(preorder, inorder)