class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        used = [False] * len(nums)

        def backtrack(start, k_remaining, curr_sum):
            if k_remaining == 0:
                return True

            if curr_sum == target:
                return backtrack(0, k_remaining - 1, 0)

            for i in range(start, len(nums)):
                if used[i]:
                    continue

                if curr_sum + nums[i] > target:
                    continue

                used[i] = True

                if backtrack(i + 1, k_remaining, curr_sum + nums[i]):
                    return True

                used[i] = False

                # pruning: avoid duplicate work
                if curr_sum == 0:
                    break

            return False

        return backtrack(0, k, 0)