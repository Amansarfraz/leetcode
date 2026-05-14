class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        
        res = []

        def dfs(num, length):
            if length == n:
                res.append(num)
                return
            
            last = num % 10

            next_digits = set([last + k, last - k])

            for d in next_digits:
                if 0 <= d <= 9:
                    dfs(num * 10 + d, length + 1)

        for i in range(1, 10):
            dfs(i, 1)

        return res