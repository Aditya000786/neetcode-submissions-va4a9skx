class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = [float('-inf')] + nums1 + [float('inf')]
        nums2 = [float('-inf')] + nums2 + [float('inf')]

        A, B = nums1, nums2
        if len(A)>len(B):
            A, B = B, A
        total = len(A)+len(B)
        half = total//2
        leftA, rightA = 0, len(A)-1
        print("t,h", total, half)
        while True:
            midA = (leftA + rightA)//2
            midB = (half - midA - 2)
            print("mid", midA, midB)
            if A[midA]>B[midB+1]:
                rightA = midA-1
            elif B[midB]>A[midA+1]:
                leftA = midA+1
            else:
                if total%2 == 0:
                    # print("even", max(nums1[midA], nums2[midB]), min(nums1[midA+1], nums2[midB]))
                    return (max(A[midA], B[midB]) + min(A[midA+1], B[midB+1]))/2
                else:
                    return min(A[midA+1], B[midB+1])