class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            a_num = abs(num)
            ind = a_num-1
            if nums[ind]<0:
                return a_num
            nums[ind]*=-1
