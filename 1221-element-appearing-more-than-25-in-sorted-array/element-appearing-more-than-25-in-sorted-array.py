class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)

        for i in [n // 4, n // 2, 3 * n // 4]:
            candidate = arr[i]

            left = self.lower_bound(arr, candidate)
            right = self.upper_bound(arr, candidate)

            if right - left > n // 4:
                return candidate

    def lower_bound(self, arr, target):
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def upper_bound(self, arr, target):
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left