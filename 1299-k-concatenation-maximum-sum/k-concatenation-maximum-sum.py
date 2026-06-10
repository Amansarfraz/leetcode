class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def kadane(nums):
            best = curr = 0
            for x in nums:
                curr = max(0, curr + x)
                best = max(best, curr)
            return best

        total = sum(arr)

        if k == 1:
            return kadane(arr) % MOD

        best = kadane(arr * 2)

        if total > 0:
            best += (k - 2) * total

        return best % MOD