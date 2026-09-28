import bisect

class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # lis_len[i] stores the length of LIS ending at nums[i]
        lis_len = [1] * n
        tails = []
        for i in range(n):
            idx = bisect.bisect_left(tails, nums[i])
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
            lis_len[i] = idx + 1
            
        # lds_len[i] stores the length of LDS starting at nums[i] (or LIS from right to left)
        lds_len = [1] * n
        tails = []
        for i in range(n - 1, -1, -1):
            idx = bisect.bisect_left(tails, nums[i])
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
            lds_len[i] = idx + 1
            
        max_mountain_len = 0
        
        # Find the peak element
        for i in range(1, n - 1):
            # A valid mountain peak must have at least one element to its left and right
            if lis_len[i] > 1 and lds_len[i] > 1:
                mountain_len = lis_len[i] + lds_len[i] - 1
                max_mountain_len = max(max_mountain_len, mountain_len)
                
        return n - max_mountain_len
