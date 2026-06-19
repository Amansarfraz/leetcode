class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, max(arr)

        while left < right:
            mid = (left + right) // 2

            total = sum(min(x, mid) for x in arr)

            if total < target:
                left = mid + 1
            else:
                right = mid

        s1 = sum(min(x, left) for x in arr)
        s2 = sum(min(x, left - 1) for x in arr)

        if abs(s2 - target) <= abs(s1 - target):
            return left - 1
        return left