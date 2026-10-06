from collections import deque

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # dp[i] stores the maximum score to reach index i
        dp = [0] * n
        dp[0] = nums[0]
        
        # Monotonic deque to store indices of dp. 
        # Elements are arranged in descending order of their dp values.
        queue = deque([0])
        
        for i in range(1, n):
            # 1. Remove indices that are out of the jump range 'k'
            if queue[0] < i - k:
                queue.popleft()
                
            # 2. The max dp value within range is always at the front of the queue
            dp[i] = nums[i] + dp[queue[0]]
            
            # 3. Maintain the monotonic property (descending order of values)
            # Remove indices from the back whose dp values are less than or equal to dp[i]
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()
                
            # 4. Add the current index to the queue
            queue.append(i)
            
        return dp[-1]
