class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = []
        ans = []
        low = 0
        for high in range(len(nums)):
            new_num = nums[high]
            while que and new_num>que[-1][0]:
                que.pop()
            que.append((new_num, high))

            while high - low >= k:
                low+=1
            
            while que and low>que[0][1]:
                que.pop(0)
            
            if high-low == k-1:
                ans.append(que[0][0])
        
        return ans