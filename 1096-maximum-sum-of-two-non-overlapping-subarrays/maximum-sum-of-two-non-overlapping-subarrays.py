class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """

        def helper(L, M):
            n = len(nums)

            prefix = [0] * (n + 1)

            for i in range(n):
                prefix[i + 1] = prefix[i] + nums[i]

            maxL = 0
            ans = 0

            for i in range(L + M, n + 1):

                maxL = max(
                    maxL,
                    prefix[i - M] - prefix[i - M - L]
                )

                currentM = prefix[i] - prefix[i - M]

                ans = max(ans, maxL + currentM)

            return ans

        return max(
            helper(firstLen, secondLen),
            helper(secondLen, firstLen)
        )