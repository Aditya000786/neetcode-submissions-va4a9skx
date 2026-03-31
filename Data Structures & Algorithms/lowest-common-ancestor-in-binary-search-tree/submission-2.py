# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_path(curr_node: TreeNode, target:TreeNode, path: List[TreeNode]):
            if not curr_node:
                return False
            path.append(curr_node)
            # print(curr_node.val, target.val)
            if curr_node.val == target.val:
                # print("path on find", path)
                return True

            if find_path(curr_node.left, target, path):
                return True

            if find_path(curr_node.right, target, path):
                return True
            path.pop()
            return False
        p_path, q_path = [],[]
        find_path(root, p, p_path)
        find_path(root, q, q_path)
        p_i,q_i=0,0
        ans = root
        print(p_path)
        print(q_path)
        while p_i<len(p_path) and q_i<len(q_path):
            if p_path[p_i] == q_path[q_i]:
                ans = p_path[p_i]
                p_i+=1
                q_i+=1
            else:
                break
        return ans

