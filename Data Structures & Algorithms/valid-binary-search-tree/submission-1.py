class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     res = []
    #     def dfs(node: Optional[TreeNode]):
    #         if node:
    #             dfs(node.left)
    #             res.append(node.val)
    #             dfs(node.right)
    #         else:
    #             return
    #     dfs(root)
    #     for i in range(1, len(res)):
    #         if res[i]<=res[i-1]:
    #             return False
    #     # return res
    #     return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node:TreeNode, left, right):
            if not node:
                return True
            if not(left<node.val<right):
                return False
            
            return (is_valid(node.left, left, node.val) and is_valid(node.right, node.val, right))

        return is_valid(root, float('-inf'), float('inf'))
        