class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse=True)

        total = sum(nums)
        curr = 0
        ans = []

        for num in nums:
            curr += num
            ans.append(num)
            if curr > total - curr:
                break

        return ans