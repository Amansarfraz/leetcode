class Solution(object):
    def arrayNesting(self, nums):
        visited = set()
        max_len = 0

        for i in range(len(nums)):
            if i not in visited:
                start = i
                count = 0

                while start not in visited:
                    visited.add(start)
                    start = nums[start]
                    count += 1

                max_len = max(max_len, count)

        return max_len