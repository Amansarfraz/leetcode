class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        n = len(nums)

        # Step 1: window sums
        window = [0] * (n - k + 1)
        curr = sum(nums[:k])
        window[0] = curr

        for i in range(1, n - k + 1):
            curr += nums[i + k - 1] - nums[i - 1]
            window[i] = curr

        m = len(window)

        # Step 2: best left index
        left = [0] * m
        best = 0

        for i in range(m):
            if window[i] > window[best]:
                best = i
            left[i] = best

        # Step 3: best right index
        right = [0] * m
        best = m - 1

        for i in range(m - 1, -1, -1):
            if window[i] >= window[best]:
                best = i
            right[i] = best

        # Step 4: try middle
        res = [-1, -1, -1]
        max_sum = 0

        for j in range(k, m - k):
            i = left[j - k]
            l = right[j + k]

            total = window[i] + window[j] + window[l]

            if total > max_sum:
                max_sum = total
                res = [i, j, l]

        return res