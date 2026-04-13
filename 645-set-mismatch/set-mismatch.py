class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        seen = set()
        duplicate = -1

        # find duplicate
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        # find missing
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]