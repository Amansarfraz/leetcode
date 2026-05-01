from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in sorted(count):

            while count[num] > 0:   # 🔥 FIX HERE

                for i in range(groupSize):
                    if count[num + i] <= 0:
                        return False
                    count[num + i] -= 1

        return True