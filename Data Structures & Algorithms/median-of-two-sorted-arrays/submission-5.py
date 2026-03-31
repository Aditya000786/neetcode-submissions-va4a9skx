class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<len(nums2):
            nums1, nums2 = nums2, nums1
        nums1 = [float('-inf')] + nums1 + [float('inf')]
        nums2 = [float('-inf')] + nums2 + [float('inf')]
        total_elem = len(nums1) + len(nums2)
        f_low, f_high = 0, len(nums1) - 1
        while f_low < f_high:
            f_pivot = (f_low + f_high)//2
            s_pivot = math.ceil(total_elem/2) - (f_pivot + 1) - 1
            if nums1[f_pivot] <= nums2[s_pivot+1] and nums2[s_pivot]<=nums1[f_pivot+1]:
                if total_elem%2 !=0:
                    return max(nums1[f_pivot], nums2[s_pivot])
                else:
                    return (max(nums1[f_pivot], nums2[s_pivot]) + min(nums1[f_pivot+1],
                    nums2[s_pivot+1])) / 2
            elif nums1[f_pivot]>nums2[s_pivot+1]:
                f_high = f_pivot-1
            else:
                f_low = f_pivot + 1
        