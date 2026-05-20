class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        flipped = [0] * n
        flip_count = 0
        ans = 0

        for i in range(n):
            if i >= k:
                flip_count ^= flipped[i - k]

            # Current bit after flips
            if nums[i] ^ flip_count == 0:
                if i + k > n:
                    return -1

                ans += 1
                flip_count ^= 1
                flipped[i] = 1

        return ans