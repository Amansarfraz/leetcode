class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []  # stores indices
        
        # iterate twice to simulate circular array
        for i in range(2 * n):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                idx = stack.pop()
                res[idx] = num
            if i < n:
                stack.append(i)
        
        return res