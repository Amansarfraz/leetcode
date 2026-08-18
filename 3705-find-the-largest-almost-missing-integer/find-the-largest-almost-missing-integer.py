import collections

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # Case 1: The window size equals the array length.
        # There is only 1 subarray, so every element appears exactly once.
        if k == n:
            return max(nums)
        
        # Global frequency map of elements across the entire array.
        count = collections.Counter(nums)
        
        # Case 2: Window size is 1.
        # Each index is its own subarray. The element must appear exactly once in total.
        if k == 1:
            valid_nums = [num for num in nums if count[num] == 1]
            return max(valid_nums) if valid_nums else -1
            
        # Case 3: 1 < k < n.
        # Elements in the middle will always appear in multiple overlapping windows.
        # Only the absolute boundary elements (nums[0] and nums[-1]) can appear in exactly 1 window.
        ans = -1
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])
        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans
