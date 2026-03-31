class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x,y = len(nums1), len(nums2)
        low,high = 0,len(nums1)
        if y==0:
            return (nums1[x//2 - 1] + nums1[x//2])%2 if x%2 == 0 else nums1[x//2]
        elif x==0:
            return (nums2[y//2 - 1] + nums2[y//2])/2 if y%2 == 0 else nums2[y//2]
        while low<=high:
            mid = (low+high)//2
            partition_x_ind = mid 
            partition_y_ind = (x+y+1)//2 - partition_x_ind

            if partition_y_ind == y:
                right_y = float('inf')
                left_y = nums2[y-1]
            if partition_y_ind == 0:
                left_y = float('-inf')
                right_y = nums2[0]
            
            if partition_x_ind == x:
                right_x = float('inf')
                left_x = nums1[x-1]
            if partition_x_ind == 0:
                left_x = float('-inf')
                right_x = nums1[0]
                
            if 0<partition_x_ind<x:
                left_x = nums1[partition_x_ind-1]
                right_x = nums1[partition_x_ind]
            
            if 0<partition_y_ind<y:
                right_y = nums2[partition_y_ind]
                left_y = nums2[partition_y_ind-1]

            if left_x <= right_y and left_y <= right_x:
                    if (x+y)%2 != 0:
                        return max(left_x, left_y)
                    else:
                        return (max(left_x, left_y) + min(right_x, right_y))/2
            else:
                if left_x>right_y:
                    high = mid-1
                    # new_high = (low+high) // 2
                    # if high == new_high:
                    #     high = new_high-1
                    # else:
                    #     high = new_high
                elif right_x < left_y:
                    low = mid+1
                    # new_low = (low+high) // 2
                    # if low == new_low:
                    #     low = new_low+1
                    # else:
                    #     low = new_low
