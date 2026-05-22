class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        count = [0] * 60
        ans = 0
        
        for t in time:
            rem = t % 60
            complement = (60 - rem) % 60
            
            ans += count[complement]
            count[rem] += 1
        
        return ans