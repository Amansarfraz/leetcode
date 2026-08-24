class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Step 1: Calculate prefix sums to find the value of taking 'i' stones
        n = len(stones)
        prefix_sum = [0] * n
        prefix_sum[0] = stones[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + stones[i]
            
        # Step 2: Base case 
        # If Alice takes all stones (index n-1), Bob gets 0 remaining choices.
        # Score difference is prefix_sum[n-1] - 0
        dp = prefix_sum[-1]
        
        # Step 3: Iterate backwards from the second-to-last possible move down to index 1
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix_sum[i] - dp)
            
        return dp
