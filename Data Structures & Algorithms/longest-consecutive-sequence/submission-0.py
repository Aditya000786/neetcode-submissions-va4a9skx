class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            # Check for lower number
            if num-1 not in hash_map and num+1 not in hash_map:
                hash_map[num] = [num]
                continue

            lower_array, upper_array = None, None
            if num-1 in hash_map:
                lower_array = hash_map[num-1]
                smallest_num = lower_array[0]
                hash_map[num] = lower_array + [num]
                hash_map[smallest_num] = lower_array + [num]

            if num+1 in hash_map:
                upper_array = hash_map[num+1]
                if lower_array:
                    hash_map[smallest_num] = hash_map[smallest_num] + upper_array
                    hash_map[upper_array[-1]] = hash_map[smallest_num] + upper_array
                else:
                    hash_map[num] = [num] + upper_array
                    hash_map[upper_array[-1]] = [num] + upper_array
            
            
        ans = 0
        for key, values in hash_map.items():
            ans = max(ans, len(set(values)))
        return ans