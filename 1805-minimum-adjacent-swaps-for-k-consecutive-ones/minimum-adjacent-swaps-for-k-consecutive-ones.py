class Solution(object):
    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Record the original indices of all 1s
        ones = [i for i, num in enumerate(nums) if num == 1]
        
        # Step 2: Transform indices to account for the space they will occupy when grouped.
        # This reduces the problem to finding the minimum absolute deviations to a median.
        for i in range(len(ones)):
            ones[i] -= i
            
        # Step 3: Create a prefix sum array to calculate range sums in O(1) time
        n = len(ones)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + ones[i]
            
        min_moves = float('inf')
        
        # Step 4: Use a sliding window of size k over the transformed 'ones' array
        for i in range(n - k + 1):
            left = i
            right = i + k - 1
            mid = left + (right - left) // 2
            median_val = ones[mid]
            
            # Number of elements on the left and right side of the median in the window
            left_count = mid - left
            right_count = right - mid
            
            # Calculate sum of elements in the left and right halves using prefix sums
            left_sum = presum[mid] - presum[left]
            right_sum = presum[right + 1] - presum[mid + 1]
            
            # Total moves for the current window based on distance to the median
            current_moves = (median_val * left_count - left_sum) + (right_sum - median_val * right_count)
            min_moves = min(min_moves, current_moves)
            
        return min_moves
