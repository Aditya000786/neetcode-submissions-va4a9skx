class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = list(range(n))
        used = []
        count = [0] * n
        for start, end in meetings:
            while used and used[0][0]<=start:
                _, used_room = heapq.heappop(used)
                heapq.heappush(available, used_room)
            # If rooms are not available
            if len(available) == 0:
                used_end_time, used_room = heapq.heappop(used)
                end += used_end_time - start
                heapq.heappush(available, used_room)
            
            new_room = heapq.heappop(available)
            # If rooms are not available
            heapq.heappush(used, (end,new_room))
            count[new_room] += 1
        
        return count.index(max(count))