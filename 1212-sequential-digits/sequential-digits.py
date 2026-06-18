class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = "123456789"
        res = []

        for length in range(2, 10):  # possible lengths
            for i in range(0, 10 - length):
                num = int(s[i:i + length])
                if low <= num <= high:
                    res.append(num)

        return sorted(res)