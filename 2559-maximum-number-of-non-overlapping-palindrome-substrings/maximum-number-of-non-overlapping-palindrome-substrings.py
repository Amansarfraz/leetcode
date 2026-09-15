class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # dp[i] stores the maximum number of non-overlapping palindromes in s[0...i-1]
        dp = [0] * (n + 1)
        
        for i in range(n):
            # By default, carry forward the optimal result from the previous character
            dp[i + 1] = max(dp[i + 1], dp[i])
            
            # Check for a palindrome of length k ending at index i
            if i - k + 1 >= 0:
                sub_k = s[i - k + 1 : i + 1]
                if sub_k == sub_k[::-1]:
                    dp[i + 1] = max(dp[i + 1], dp[i - k + 1] + 1)
                    
            # Check for a palindrome of length k + 1 ending at index i
            if i - k >= 0:
                sub_k1 = s[i - k : i + 1]
                if sub_k1 == sub_k1[::-1]:
                    dp[i + 1] = max(dp[i + 1], dp[i - k] + 1)
                    
        return dp[n]
