class Solution(object):
    def numDecodings(self, s):
        MOD = 10**9 + 7
        
        n = len(s)
        if n == 0:
            return 0
        
        # dp[i-2], dp[i-1]
        prev2 = 1
        
        # First character
        if s[0] == '0':
            return 0
        elif s[0] == '*':
            prev1 = 9
        else:
            prev1 = 1
        
        for i in range(1, n):
            curr = 0
            
            # -------- Single digit --------
            if s[i] == '*':
                curr += 9 * prev1
            elif s[i] != '0':
                curr += prev1
            
            # -------- Two digits --------
            if s[i-1] == '1':
                if s[i] == '*':
                    curr += 9 * prev2
                else:
                    curr += prev2
            
            elif s[i-1] == '2':
                if s[i] == '*':
                    curr += 6 * prev2
                elif '0' <= s[i] <= '6':
                    curr += prev2
            
            elif s[i-1] == '*':
                if s[i] == '*':
                    curr += 15 * prev2   # 11–19 and 21–26
                elif '0' <= s[i] <= '6':
                    curr += 2 * prev2    # (1x, 2x)
                else:
                    curr += prev2        # only (1x)
            
            curr %= MOD
            
            prev2 = prev1
            prev1 = curr
        
        return prev1