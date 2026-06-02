class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        n = mountainArr.length()

        # Find peak element
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        # Binary search in ascending part
        left, right = 0, peak
        while left <= right:
            mid = left + (right - left) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search in descending part
        left, right = peak + 1, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val > target:  # reversed comparison
                left = mid + 1
            else:
                right = mid - 1

        return -1
    