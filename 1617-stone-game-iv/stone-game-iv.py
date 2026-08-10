class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # dp[i] stores if a player can win with i stones
        dp = [False] * (n + 1)
        
        # Iteratively calculate winning states up to n
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                # If subtracting k*k puts the opponent in a losing state
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # Found a winning move, no need to check further
                k += 1
                
        return dp[n]
