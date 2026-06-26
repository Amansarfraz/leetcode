from collections import defaultdict

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = defaultdict(int)

        for num in range(1, n + 1):
            s = 0
            x = num
            while x:
                s += x % 10
                x //= 10
            count[s] += 1

        largest = max(count.values())
        ans = 0

        for freq in count.values():
            if freq == largest:
                ans += 1

        return ans