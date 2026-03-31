class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0]<=ans[-1][1]:
                ans[-1][0], ans[-1][1] = min(ans[-1][0], curr[0]), max(ans[-1][1], curr[1])
            else:
                ans.append(curr)
        return ans