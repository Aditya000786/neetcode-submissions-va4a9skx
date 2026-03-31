import heapq
class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_heap, -num)
        while len(self.left_heap) - len(self.right_heap)>1:
            temp = -1*heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, temp)
        while self.right_heap and -1*self.left_heap[0]>self.right_heap[0]:
            left_val = -1*heapq.heappop(self.left_heap)
            right_val = heapq.heappop(self.right_heap)
            heapq.heappush(self.right_heap, left_val)
            heapq.heappush(self.left_heap, -right_val)
            

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0])/2
        else:
            return -self.left_heap[0]
        