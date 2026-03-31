import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = max(piles)

        def calc_time(k:int) -> int:
            used = 0
            for i in range(len(piles)):
                used += math.ceil(piles[i]/k)
            return used

        while low<=high:
            mid = (low + high)//2
            time = calc_time(mid)
            if time>h:
                low = mid + 1
            elif time<=h:
                high = mid - 1
                # ans = min(ans, mid)
                ans = mid
        return ans