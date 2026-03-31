class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        else:
            adj_list = defaultdict(list)
            for n1, n2 in edges:
                adj_list[n1].append(n2)
                adj_list[n2].append(n1)
            print(adj_list)
            
            def dfs(node, parent):
                if node in visited:
                    return True
                visited.add(node)
                neigh = adj_list[node]
                for ne in neigh:
                    if ne in visited and ne!=parent:
                        return False
                    else:
                        dfs(ne, node)
                return True
            
            for node in adj_list.keys():
                visited = set()
                if not dfs(node, None):
                    return False
            return True
        