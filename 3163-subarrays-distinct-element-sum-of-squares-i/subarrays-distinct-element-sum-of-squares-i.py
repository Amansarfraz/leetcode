class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in range(n):
            num_set = set()
            for j in range(i, n):
                num_set.add(nums[j])
                res += len(num_set) ** 2
        return res
