from collections import defaultdict

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        count[0] = 1

        prefix = 0
        ans = 0

        for num in nums:
            prefix += num % 2

            ans += count[prefix - k]

            count[prefix] += 1

        return ans