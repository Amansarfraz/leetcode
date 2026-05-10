class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        from collections import defaultdict

        freq = defaultdict(int)
        freq[0] = 1

        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            if prefix - goal in freq:
                count += freq[prefix - goal]

            freq[prefix] += 1

        return count
        