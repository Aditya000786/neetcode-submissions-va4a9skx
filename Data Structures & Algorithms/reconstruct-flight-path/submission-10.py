class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in sorted(tickets)[::-1]:
            graph[src].append(dest)
        ans = []
        print(graph)
        def dfs(node):
            # for i in range(len(graph[node])):
            while graph[node]:
                next = graph[node].pop()
                dfs(next)
            ans.append(node)
            print("ans", ans)
        dfs("JFK")
        ans = ans[::-1]
        print(ans)
        return ans