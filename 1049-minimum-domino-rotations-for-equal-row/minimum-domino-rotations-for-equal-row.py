class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        
        def check(x):
            top_rotate = 0
            bottom_rotate = 0
            
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                
                if tops[i] != x:
                    top_rotate += 1
                
                if bottoms[i] != x:
                    bottom_rotate += 1
            
            return min(top_rotate, bottom_rotate)
        
        ans = check(tops[0])
        
        if ans != -1:
            return ans
        
        return check(bottoms[0])