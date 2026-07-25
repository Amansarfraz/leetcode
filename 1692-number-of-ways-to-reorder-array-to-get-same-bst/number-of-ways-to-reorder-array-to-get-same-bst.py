class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)

        # Pascal Triangle for nCr
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = []
            right = []

            for x in arr[1:]:
                if x < root:
                    left.append(x)
                else:
                    right.append(x)

            leftWays = dfs(left)
            rightWays = dfs(right)

            return (comb[len(left) + len(right)][len(left)] *
                    leftWays % MOD *
                    rightWays) % MOD

        return (dfs(nums) - 1) % MOD