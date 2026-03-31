from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)                          # O(n)
        # buckets[i] = list of numbers that occur exactly i times
        buckets = [[] for _ in range(len(nums) + 1)]  # frequencies range 0..n
        for val, f in freq.items():                   # O(m) ≤ O(n)
            buckets[f].append(val)

        res = []
        # Traverse frequencies from high to low
        for f in range(len(nums), 0, -1):             # O(n)
            if buckets[f]:
                for val in buckets[f]:
                    res.append(val)
                    if len(res) == k:
                        return res
        return res  # in case k > number of uniques
