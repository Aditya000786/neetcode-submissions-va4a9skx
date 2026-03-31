class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        suf = [0] * len(height)
        curr_pre_max = 0
        curr_suf_max = 0
        for i in range(1, len(height)):
            pre[i] = max(pre[i-1], height[i-1])
        for j in range(len(height)-2, -1, -1):
            suf[j] = max(suf[j+1], height[j+1])
        ans = 0
        for i in range(1, len(height)-1):
            curr_height = max(min(pre[i], suf[i]) - height[i], 0)
            ans += curr_height
        return ans