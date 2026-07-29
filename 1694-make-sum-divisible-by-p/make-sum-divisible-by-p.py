class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0

        prefix = 0
        seen = {0: -1}
        ans = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - rem) % p

            if target in seen:
                ans = min(ans, i - seen[target])

            seen[prefix] = i

        return ans if ans < len(nums) else -1