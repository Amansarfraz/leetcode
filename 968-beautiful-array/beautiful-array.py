class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [1]

        while len(res) < n:
            temp = []

            # odd numbers
            for x in res:
                if 2*x - 1 <= n:
                    temp.append(2*x - 1)

            # even numbers
            for x in res:
                if 2*x <= n:
                    temp.append(2*x)

            res = temp

        return res