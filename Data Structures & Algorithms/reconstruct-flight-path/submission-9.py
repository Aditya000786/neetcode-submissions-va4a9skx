class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)

        trips_taken = 0
        ans = ["JFK"]
        def dfs(node):
            nonlocal trips_taken
            for ind in range(len(graph[node])):
                neigh = graph[node].pop(ind)
                ans.append(neigh)
                trips_taken+=1
                if dfs(neigh):
                    return True
                ans.pop()
                trips_taken-=1
                graph[node].insert(ind, neigh)
            return True if trips_taken == len(tickets) else False
        dfs("JFK")
        return ans
