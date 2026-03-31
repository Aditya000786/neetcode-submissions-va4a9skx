class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = None
        for trip in triplets:
            if trip[0]<=target[0] and trip[1]<=target[1] and trip[2]<=target[2]:
                if not ans:
                    ans = trip
                    continue
                for i in range(3):
                    ans[i] = max(ans[i], trip[i])
        return ans == target