class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        c = Counter(hand)
        ind = 0
        while True:
            while ind < len(hand) and hand[ind] not in c:
                ind += 1
            if ind > len(hand) - 1:
                return True
            start = hand[ind]
            for curr in range(start, start + groupSize):
                if curr in c:
                    c[curr]-=1
                    if c[curr]==0:
                        del c[curr]
                else:
                    return False
        return True
