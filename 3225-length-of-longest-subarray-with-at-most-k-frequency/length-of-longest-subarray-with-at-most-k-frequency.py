class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        frequency = {}
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Add the current element to the frequency map
            current_num = nums[right]
            frequency[current_num] = frequency.get(current_num, 0) + 1
            
            # Shrink the window from the left if the frequency exceeds k
            while frequency[current_num] > k:
                left_num = nums[left]
                frequency[left_num] -= 1
                left += 1
                
            # Update the maximum length of a valid subarray
            max_length = max(max_length, right - left + 1)
            
        return max_length
