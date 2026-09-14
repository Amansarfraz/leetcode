class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10**9 + 7
        w_len = len(words[0])
        t_len = len(target)
        
        # Step 1: Precompute character frequencies for each column index
        # char_counts[col][char] stores how many times 'char' appears at index 'col'
        char_counts = [[0] * 26 for _ in range(w_len)]
        for word in words:
            for col, char in enumerate(word):
                char_counts[col][ord(char) - ord('a')] += 1
                
        # Step 2: DP array where dp[j] is the number of ways to form target[:j]
        # dp[0] = 1 represents the base case (1 way to form an empty target)
        dp = [1] + [0] * t_len
        
        # Step 3: Iterate through each column of words
        for col in range(w_len):
            # Iterate backwards to use values from the previous column's state
            for j in range(t_len - 1, -1, -1):
                target_char = target[j]
                count = char_counts[col][ord(target_char) - ord('a')]
                
                if count > 0:
                    dp[j + 1] = (dp[j + 1] + dp[j] * count) % MOD
                    
        return dp[t_len]
