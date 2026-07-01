class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        for den in range(2, n + 1):
            for num in range(1, den):
                if self.gcd(num, den) == 1:
                    ans.append(str(num) + "/" + str(den))

        return ans