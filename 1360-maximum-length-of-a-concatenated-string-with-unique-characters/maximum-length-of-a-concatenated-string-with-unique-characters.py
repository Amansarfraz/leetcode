class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        valid = []

        for s in arr:
            if len(set(s)) == len(s):
                valid.append(set(s))

        self.ans = 0

        def dfs(i, used):
            self.ans = max(self.ans, len(used))

            for j in range(i, len(valid)):
                if not (used & valid[j]):   # no common characters
                    dfs(j + 1, used | valid[j])

        dfs(0, set())
        return self.ans