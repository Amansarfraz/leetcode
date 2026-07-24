class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = 2048

        freq = [0] * MAX
        for x in nums:
            freq[x] = 1

        a = freq[:]

        step = 1
        while step < MAX:
            for i in range(0, MAX, step * 2):
                for j in range(i, i + step):
                    x = a[j]
                    y = a[j + step]
                    a[j] = x + y
                    a[j + step] = x - y
            step <<= 1

        for i in range(MAX):
            a[i] = a[i] * a[i] * a[i]

        step = 1
        while step < MAX:
            for i in range(0, MAX, step * 2):
                for j in range(i, i + step):
                    x = a[j]
                    y = a[j + step]
                    a[j] = x + y
                    a[j + step] = x - y
            step <<= 1

        ans = 0
        for i in range(MAX):
            if a[i] != 0:
                ans += 1

        return ans