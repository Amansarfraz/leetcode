from collections import Counter

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        freq = Counter(arr)
        counts = sorted(freq.values())

        unique = len(counts)

        for c in counts:
            if k >= c:
                k -= c
                unique -= 1
            else:
                break

        return unique