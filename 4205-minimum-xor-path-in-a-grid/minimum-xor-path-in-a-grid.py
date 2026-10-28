class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # dp[j] will store the set of all possible XOR sums reachable at column j
        dp = [set() for _ in range(n)]
        
        # Initialize the starting cell
        dp[0].add(grid[0][0])
        
        # Fill the first row (can only come from the left)
        for j in range(1, n):
            for val in dp[j-1]:
                dp[j].add(val ^ grid[0][j])
                
        # Fill the remaining rows
        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            
            # For the first column of the new row (can only come from above)
            for val in dp[0]:
                new_dp[0].add(val ^ grid[i][0])
                
            # For the remaining columns (can come from above or left)
            for j in range(1, n):
                # From above (dp[j])
                for val in dp[j]:
                    new_dp[j].add(val ^ grid[i][j])
                # From left (new_dp[j-1])
                for val in new_dp[j-1]:
                    new_dp[j].add(val ^ grid[i][j])
                    
            dp = new_dp
            
        # The answer is the minimum value in the bottom-right cell's set
        return min(dp[n-1])
