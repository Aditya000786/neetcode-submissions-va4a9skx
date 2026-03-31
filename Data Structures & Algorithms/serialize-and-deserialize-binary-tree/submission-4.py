# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def bfs(node):
            if not node:
                return "None"
            que = deque([root])
            while que:
                level = []
                for i in range(len(que)):
                    curr = que.popleft()
                    if not curr:
                        level.append("None")
                        continue
                    level.append(str(curr.val))
                    que.append(curr.left)
                    que.append(curr.right)
                temp = ",".join(level)
                ans.append(temp)
            temp = "||".join(ans)
            print("temp", temp)
            return temp
        return bfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        levels = data.split("||")
        root = None
        pre_levels = []
        ind = 0
        while ind<len(levels):
            curr_level_val = levels[ind].split(",")
            curr_level_nodes = []
            for i in range(len(curr_level_val)):
                if curr_level_val[i]=="None":
                    continue
                node = TreeNode(int(curr_level_val[i]))
                curr_level_nodes.append(node)
                parent_ind = i//2
                is_even = i%2==0
                if not pre_levels:
                    pre_levels.append(node)
                    root = node
                else:
                    if is_even:
                        pre_levels[parent_ind].left = node
                    else:
                        pre_levels[parent_ind].right = node
            pre_levels = curr_level_nodes
            ind+=1
        return root
