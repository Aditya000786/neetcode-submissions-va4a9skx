class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        def ksum(n: int, target: int, left: int, right: int) -> List[int]:
            ans = []
            if n == 2:
                while left<right:
                    if nums[left] + nums[right] == target:
                        ans.append([nums[left], nums[right]])
                        left+=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                    if nums[left] + nums[right] > target:
                        right-=1
                    else:
                        left+=1
            else:
                while left<right:
                    rec_ans = ksum(n-1, target-nums[left], left+1, right)
                    if rec_ans:
                        ans.extend([t + [nums[left]] for t in rec_ans])
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
            return ans
        return ksum(3, target, 0, len(nums)-1)