class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        # If the required sum exceeds the maximum possible sum of num 9's
        if num * 9 < sum:
            return ""
        
        # Calculate the number of 9's (k) and the leftover remainder (s)
        k, s = divmod(sum, 9)
        
        # Place the 9's at the most significant positions
        ans = "9" * k
        if s > 0:
            ans += str(s)
            
        # Pad the rest of the digits with 0's to reach length 'num'
        ans += "0" * (num - len(ans))
        
        return ans
