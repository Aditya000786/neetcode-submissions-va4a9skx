class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos, neg = 1, 1
        prev = 1
        res = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            curr = nums[i]
            curr_1 = curr * pos
            curr_2 = curr * neg

            res = max(res, curr, curr_1, curr_2)

            max_neg = 1
            if curr_1<0 and abs(curr_1)>=abs(max_neg):
                max_neg = curr_1
            if curr_2<0 and abs(curr_2)>=abs(max_neg):
                max_neg = curr_2
            if curr<0 and abs(curr)>=abs(max_neg):
                max_neg = curr 

            max_pos = 1
            if curr_1>max_pos:
                max_pos = curr_1
            if curr_2>max_pos:
                max_pos = curr_2
            if curr > max_pos:
                max_pos = curr 

            neg = max_neg
            pos = max_pos
        return res