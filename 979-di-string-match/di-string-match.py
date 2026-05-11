class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        low, high = 0, len(s)
        res = []
        
        for ch in s:
            if ch == 'I':
                res.append(low)
                low += 1
            else:  # 'D'
                res.append(high)
                high -= 1
        
        res.append(low)  # low == high at end
        return res