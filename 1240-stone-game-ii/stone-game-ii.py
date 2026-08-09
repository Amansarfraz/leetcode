class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        
        # Suffix sums to compute total remaining stones efficiently
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
            
        memo = {}
        
        def dfs(i, M):
            # Base case: no piles left
            if i >= n:
                return 0
            
            # Check memoized results
            if (i, M) in memo:
                return memo[(i, M)]
            
            # If current player can take all remaining piles
            if i + 2 * M >= n:
                return suffix_sums[i]
            
            # Minimize opponent's score to maximize own score
            max_stones = 0
            for X in range(1, 2 * M + 1):
                opponent_score = dfs(i + X, max(M, X))
                current_score = suffix_sums[i] - opponent_score
                max_stones = max(max_stones, current_score)
                
            memo[(i, M)] = max_stones
            return max_stones
            
        return dfs(0, 1)
