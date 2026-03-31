# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            queue = deque([root])
            no_of_child = 1
            level = 0
            while queue:
                temp = 0
                level+=1
                for i in range(no_of_child):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                        temp+=1
                    if node.right:
                        queue.append(node.right)
                        temp+=1
                no_of_child = temp
            return level
