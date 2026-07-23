class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        add = 0
        max_double = 0

        for num in nums:
            doubles = 0
            while num > 0:
                if num % 2 == 1:
                    add += 1
                num //= 2
                if num > 0:
                    doubles += 1
            max_double = max(max_double, doubles)

        return add + max_double