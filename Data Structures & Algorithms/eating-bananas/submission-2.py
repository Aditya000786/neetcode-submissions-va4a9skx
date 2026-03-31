import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = None

        def calc_time(k:int) -> int:
            used = 0
            for i in range(len(piles)):
                used += math.ceil(piles[i]/k)
            return used

        while low<=high:
            mid = (low + high)//2
            time = calc_time(mid)
            print(low, high, mid)
            print("time", time)
            if time>h:
                low = mid + 1
                if ans is not None and mid>=ans:
                    return ans
            elif time<h:
                high = mid - 1
                ans = mid
            else:
                ans = mid
                high = mid - 1
        return ans