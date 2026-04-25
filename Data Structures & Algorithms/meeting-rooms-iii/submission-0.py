class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = set(range(n))
        heap = []
        meetings.sort()
        meetings_taken = {}
        ans = 0
        max_meetings = 0
        for start, end in meetings:
            while heap and heap[0][0]<=start:
                time, room = heapq.heappop(heap)
                available_rooms.add(room)
            
            if len(available_rooms) == 0:
                prev_end_time, room = heapq.heappop(heap)
                diff = prev_end_time - start
                available_rooms.add(room)
                end = end + diff

            room_to_use = min(available_rooms)
            heapq.heappush(heap, (end, room_to_use))
            available_rooms.remove(room_to_use)
            meetings_taken[room_to_use] = meetings_taken.get(room_to_use, 0) + 1
            if meetings_taken[room_to_use] >= max_meetings:
                ans = room_to_use if meetings_taken[room_to_use] > max_meetings else min(room_to_use, ans)
                max_meetings = meetings_taken[room_to_use]
        return ans 