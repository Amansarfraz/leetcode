
class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        height = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1

            stack = []
            dp = [0] * n

            for j in range(n):
                while stack and height[stack[-1]] >= height[j]:
                    stack.pop()

                if stack:
                    prev = stack[-1]
                    dp[j] = dp[prev] + height[j] * (j - prev)
                else:
                    dp[j] = height[j] * (j + 1)

                stack.append(j)
                ans += dp[j]

        return ans