import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        map = {}
        for num in hand:
            map[num] = map.get(num, 0) + 1
        heap = []
        for key in map.keys():
            heapq.heappush(heap, key)
        while heap:
            start = heap[0]
            curr = start
            while curr<start+groupSize:
                if curr not in map: 
                    # print("amp", curr, start, groupSize)
                    return False
                map[curr]-=1
                if map[curr] == 0:
                    if curr != heap[0]: 
                        return False
                    else:
                        heapq.heappop(heap)
                curr+=1
        return True
            