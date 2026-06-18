class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2

            total = 0
            for num in nums:
                total += (num + mid - 1) // mid  # ceil(num / mid)

            if total <= threshold:
                right = mid
            else:
                left = mid + 1

        return left