from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high

        def can_eat(rate):
            total = 0
            for num in piles:
                total += ceil(num/rate)
            return total

        while low<=high:
            curr = (low+high)//2
            need = can_eat(curr)
            if need>h:
                low = curr+1
            else:
                ans = min(ans, curr)
                high = curr-1
        return ans