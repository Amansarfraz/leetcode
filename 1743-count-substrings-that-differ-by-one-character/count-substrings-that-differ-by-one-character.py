class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ans = 0
        m, n = len(s), len(t)
        
        # Check every pair of starting indices (i, j) for s and t
        for i in range(m):
            for j in range(n):
                # Only process if characters don't match (found the 1 mismatch)
                if s[i] != t[j]:
                    # Count matching characters to the left
                    left = 0
                    while i - left > 0 and j - left > 0 and s[i - left - 1] == t[j - left - 1]:
                        left += 1
                        
                    # Count matching characters to the right
                    right = 0
                    while i + right + 1 < m and j + right + 1 < n and s[i + right + 1] == t[j + right + 1]:
                        right += 1
                        
                    # Total combinations of valid substrings for this mismatch
                    ans += (left + 1) * (right + 1)
                    
        return ans
