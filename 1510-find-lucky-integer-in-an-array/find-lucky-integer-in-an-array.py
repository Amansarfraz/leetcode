from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = Counter(arr)
        ans = -1

        for num, freq in count.items():
            if num == freq:
                ans = max(ans, num)

        return ans