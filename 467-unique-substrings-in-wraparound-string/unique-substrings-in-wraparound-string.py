class Solution(object):
    def findSubstringInWraproundString(self, s):
        dp = [0] * 26
        k = 0  # current length of valid substring
        
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                k += 1
            else:
                k = 1
            
            idx = ord(s[i]) - ord('a')
            dp[idx] = max(dp[idx], k)
        
        return sum(dp)