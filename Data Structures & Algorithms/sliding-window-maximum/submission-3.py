class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_deque: list = []
        res = []
        l,r=0,0
        while r<len(nums):
            # Remove out of bounds elements
            while mono_deque:
                left_most_ind, left_most_val = mono_deque[0]
                if left_most_ind<l:
                    mono_deque.pop(0)
                else:
                    break
            
            # Insert by making sure that queue is in decreasing order
            while mono_deque:
                _, right_most = mono_deque[-1]
                if nums[r]>right_most:
                    mono_deque.pop(-1)
                else:
                    break
                    
            mono_deque.append((r, nums[r]))
            if r>=k-1:
                res.append(mono_deque[0][1])
            r+=1
            if r-l<k:
                continue
            l+=1
        return res