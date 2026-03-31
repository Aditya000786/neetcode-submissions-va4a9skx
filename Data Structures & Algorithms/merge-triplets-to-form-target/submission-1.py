class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = None
        second = None
        third = None
        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1]<=target[1] and triplet[2]<=target[2]:
                first = triplet
            if triplet[1] == target[1] and triplet[0]<=target[0] and triplet[2]<=target[2]:
                second = triplet
            if triplet[2] == target[2] and triplet[1]<=target[1] and triplet[0]<=target[0]:
                third = triplet
        if first and second and third:
            return True
        return False