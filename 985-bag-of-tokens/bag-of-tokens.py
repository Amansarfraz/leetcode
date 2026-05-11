class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        
        i, j = 0, len(tokens) - 1
        score = 0
        best = 0
        
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
                best = max(best, score)
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        
        return best