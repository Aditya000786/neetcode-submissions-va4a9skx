class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        post = [1]*len(nums)
        ans = []
        for i in range(len(nums)):
            pre_ind = i
            post_ind = len(nums)-i-1
            if pre_ind>0:
                pre[pre_ind] = pre[pre_ind-1]*nums[pre_ind-1]
            if post_ind<len(nums)-1:
                post[post_ind] = post[post_ind+1]*nums[post_ind+1]
        for j in range(len(nums)):
            ans.append(pre[j]*post[j])
        return ans