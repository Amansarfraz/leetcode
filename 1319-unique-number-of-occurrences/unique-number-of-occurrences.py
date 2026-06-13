from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = Counter(arr)
        return len(freq.values()) == len(set(freq.values()))