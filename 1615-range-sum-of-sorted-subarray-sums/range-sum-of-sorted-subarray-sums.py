class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MOD = 10**9 + 7
        sums = []

        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                sums.append(curr)

        sums.sort()

        return sum(sums[left - 1:right]) % MOD