class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = [0]*len(height), [0]*len(height)
        left[0],right[-1] = 0, 0
        cur_max = 0
        for i in range(1, len(height)):
            left[i] = max(cur_max, height[i-1])
            cur_max = left[i]
        cur_max = 0
        for i in range(len(height)-2,-1,-1):
            right[i] = max(cur_max, height[i+1])
            cur_max = right[i]
        ans = 0
        for i in range(len(height)):
            temp = min(left[i], right[i]) - height[i]
            if temp<0:
                temp = 0
            print(i, temp)
            ans+=temp
        # print(left)
        # print(right)
        return ans