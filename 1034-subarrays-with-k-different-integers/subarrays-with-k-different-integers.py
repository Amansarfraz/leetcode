class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(K):
            count = {}
            left = 0
            result = 0

            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1

                while len(count) > K:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1

                result += right - left + 1

            return result

        return atMost(k) - atMost(k - 1)