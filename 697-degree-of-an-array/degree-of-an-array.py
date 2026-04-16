class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from collections import defaultdict

        freq = defaultdict(int)
        first = {}
        last = {}

        for i, num in enumerate(nums):
            freq[num] += 1

            if num not in first:
                first[num] = i

            last[num] = i

        degree = max(freq.values())
        res = len(nums)

        for num in freq:
            if freq[num] == degree:
                res = min(res, last[num] - first[num] + 1)

        return res