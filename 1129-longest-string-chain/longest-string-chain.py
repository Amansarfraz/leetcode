class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        words.sort(key=len)
        
        dp = {}
        ans = 1

        for word in words:
            dp[word] = 1

            # Har character remove karke predecessor check karo
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]

                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)

            ans = max(ans, dp[word])

        return ans