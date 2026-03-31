import copy
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        org_graph = copy.deepcopy(graph)
        
        for src, dest in tickets:
            graph[src].append(dest)
        for node in graph.keys():
            graph[node].sort()
        visited_paths = set()
        ans = ["JFK"]
        # print("graph", graph)
        def dfs(node):
            temp = list(graph[node])
            for ind, dest in enumerate(temp):
                # print("node-dest", node, dest, ans)
                ans.append(dest)
                del graph[node][ind]
                if not dfs(dest):
                    # print("rein=befre", graph)
                    graph[node].insert(ind, dest)
                    # print("rein=befre", graph)
                    ans.pop()
                else:
                    return True

                # if node+"-"+dest not in visited_paths:
                #     ans.append(dest)
                #     visited_paths.add(node+"-"+dest)
                #     if not dfs(dest):
                #         visited_paths.remove(node+"-"+dest)
                #         ans.pop()
                #     else:
                #         return True
            return True if len(ans)-1 == len(tickets) else False
        dfs("JFK")
        # print(visited_paths)
        return ans