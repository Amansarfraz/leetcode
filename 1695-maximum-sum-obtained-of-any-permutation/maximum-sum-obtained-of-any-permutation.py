class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Difference array
        freq = [0] * (n + 1)

        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1

        # Prefix sum to get frequency of each index
        for i in range(1, n):
            freq[i] += freq[i - 1]

        freq = freq[:n]

        # Sort both arrays
        nums.sort()
        freq.sort()

        ans = 0
        for i in range(n):
            ans = (ans + nums[i] * freq[i]) % MOD

        return ans