class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        N = len(nums)
        curr_max = (nums[0], 0)
        curr_fuel = nums[0]
        ans = 1
        curr_pos = 0
        iter = 0 
        while curr_pos < len(nums) and iter<100000000000000000000:
            while curr_fuel>0 and curr_pos < len(nums):
                if nums[curr_pos]+curr_pos>curr_max[0] + curr_max[1]:
                    # print(ans,"ss", nums[curr_pos], curr_pos)
                    curr_max = (nums[curr_pos], curr_pos)
                curr_pos+=1
                curr_fuel-=1
                
            if curr_pos>=N-1:
                break
            if nums[curr_pos]+curr_pos>curr_max[0] + curr_max[1]:
                # print(ans,"out ss", nums[curr_pos], curr_pos)
                curr_max = (nums[curr_pos], curr_pos)
            # print("b", curr_pos, N)
            ans+=1
            curr_fuel = curr_max[0] - (curr_pos - curr_max[1])
            # print(ans,"new_cur", curr_fuel, curr_pos)
            iter+=1
        return ans