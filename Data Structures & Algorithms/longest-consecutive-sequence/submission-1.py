class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seqs = []
        for num in nums:
            if num-1 in nums:
                continue
            else:
                seq = [num]
                while num+1 in nums:
                    seq.append(num+1)
                    num+=1
                seqs.append(seq)
        ans = 0
        for seq in seqs:
            ans = max(ans, len(seq))
        return ans
