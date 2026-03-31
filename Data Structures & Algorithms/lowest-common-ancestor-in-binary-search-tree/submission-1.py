class Solution:
    def find_path(self, node: TreeNode, target:TreeNode):
        def is_node_present_path(node: TreeNode, target_node: TreeNode):
            if not node:
                return []
            if node == target_node:
                return [node]
            
            else:
                path = [node]
                left_path = is_node_present_path(node.left, target_node)
                if left_path:
                    return path + left_path
                right_path = is_node_present_path(node.right, target_node)
                if right_path:
                    return path + right_path
        return is_node_present_path(node, target)
    
    def find_common_path(self, p_path: List[TreeNode], q_path: List[TreeNode]):
        common_path = []
        i = 0
        while i<len(p_path) and i<len(q_path):
            if p_path[i] == q_path[i]:
                common_path.append(p_path[i])
                i+=1
            else:
                break
        return common_path
        
    
    def lowestCommonAncestor_without_using_bst(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.find_path(root, p)
        q_path = self.find_path(root, q)
        common_path = self.find_common_path(p_path, q_path)
        return common_path[-1]
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowestCommonAncestor_using_bst(root, p, q)
    
    def lowestCommonAncestor_using_bst(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val>curr.val and q.val>curr.val:
                curr = curr.right
            elif p.val<curr.val and q.val<curr.val:
                curr = curr.left
            else:
                break
        return curr
    