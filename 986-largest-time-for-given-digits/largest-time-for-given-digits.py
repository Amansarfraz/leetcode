class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        import itertools
        
        best = -1
        
        for perm in itertools.permutations(arr):
            h = perm[0] * 10 + perm[1]
            m = perm[2] * 10 + perm[3]
            
            if 0 <= h < 24 and 0 <= m < 60:
                best = max(best, h * 60 + m)
        
        if best == -1:
            return ""
        
        return "{:02d}:{:02d}".format(best // 60, best % 60)