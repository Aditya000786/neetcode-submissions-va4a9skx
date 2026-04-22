import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(heap)
        ans = ""
        while heap:
            cou, char = heapq.heappop(heap)
            if cou < 0:
                if len(ans)>=2 and ans[-2:] == char*2:
                    prev_cou, prev_char = cou, char
                    cou, char = heapq.heappop(heap)
                    if cou<0:
                        ans+=char
                        heapq.heappush(heap, (cou+1, char))
                        heapq.heappush(heap, (prev_cou, prev_char))
                else:
                    ans+=char
                    heapq.heappush(heap, (cou+1, char))
        return ans