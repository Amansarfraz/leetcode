class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
        if not strs:
            return 0
        
        n = len(strs[0])
        m = len(strs)
        count = 0
        
        for col in range(n):
            for row in range(m - 1):
                if strs[row][col] > strs[row + 1][col]:
                    count += 1
                    break
        
        return count