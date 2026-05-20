class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        n = len(stones)

        # Check if it is possible to merge into one pile
        if (n - 1) % (k - 1) != 0:
            return -1

        # Prefix sum for range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[i][j] = minimum cost to merge stones[i:j+1]
        dp = [[0] * n for _ in range(n)]

        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                # Try every valid partition
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j],
                                   dp[i][mid] + dp[mid + 1][j])

                # If current interval can be merged into one pile
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return dp[0][n - 1]