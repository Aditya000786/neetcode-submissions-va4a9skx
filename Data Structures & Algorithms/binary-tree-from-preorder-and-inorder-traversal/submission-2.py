# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder) -> Optional[TreeNode]:
            print("dfs",preorder, inorder)

            if len(inorder)==0 or len(preorder) == 0:
                return None
            
            root_val = preorder[0]
            root = TreeNode(root_val)

            mid = -1
            for i in range(len(inorder)):
                if inorder[i] == root_val:
                    mid = i

            left_num, right_num = len(inorder[:mid]), len(inorder[mid+1:])
            root.left = dfs(preorder[1:left_num+1], inorder[:mid])
            root.right = dfs(preorder[1+left_num:], inorder[mid+1:])

            
            # left_most_value = None if ind_of_root_inorder-1 < 0 else inorder[ind_of_root_inorder-1]
            # right_least_value = None if ind_of_root_inorder+1 >= len(preorder) else inorder[ind_of_root_inorder+1]

            # print(left_most_value, right_least_value)
            # if left_most_value:
            #     root.left = dfs(preorder[1:preorder.index(left_most_value)+1], inorder[:inorder.index(left_most_value)+1])
            # if right_least_value:
            #     root.right = dfs(preorder[preorder.index(right_least_value):], inorder[inorder.index(right_most_value):])
            return root

        return dfs(preorder, inorder)