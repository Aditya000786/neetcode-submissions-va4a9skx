class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in sorted(tickets)[::-1]:
            graph[src].append(dest)
        ans = []
        def dfs(node):
            while graph[node]:
                next = graph[node].pop()
                dfs(next)
            ans.append(node)
        dfs("JFK")
        ans = ans[::-1]
        return ans