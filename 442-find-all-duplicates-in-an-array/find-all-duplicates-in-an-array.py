class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            index = abs(num) - 1  # map value to index
            if nums[index] < 0:
                res.append(abs(num))  # already seen
            else:
                nums[index] = -nums[index]  # mark as seen
        return res