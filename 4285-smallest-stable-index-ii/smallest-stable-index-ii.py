class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        
        # Step 1: Precompute prefix maximums
        pref_max = [0] * n
        current_max = nums[0]
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            pref_max[i] = current_max
            
        # Step 2: Precompute suffix minimums
        suff_min = [0] * n
        current_min = nums[n - 1]
        for i in range(n - 1, -1, -1):
            if nums[i] < current_min:
                current_min = nums[i]
            suff_min[i] = current_min
            
        # Step 3: Find the smallest index satisfying the condition
        for i in range(n):
            if pref_max[i] - suff_min[i] <= k:
                return i
                
        return -1
