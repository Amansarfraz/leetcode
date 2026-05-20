class Solution(object):
    def numSquarefulPerms(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        import math

        count = Counter(nums)
        graph = {x: [] for x in count}

        # Build graph
        for x in count:
            for y in count:
                s = x + y
                if int(math.sqrt(s)) ** 2 == s:
                    graph[x].append(y)

        n = len(nums)

        def dfs(x, remaining):
            count[x] -= 1

            if remaining == 0:
                count[x] += 1
                return 1

            total = 0

            for nei in graph[x]:
                if count[nei] > 0:
                    total += dfs(nei, remaining - 1)

            count[x] += 1
            return total

        result = 0

        for x in count:
            result += dfs(x, n - 1)

        return result