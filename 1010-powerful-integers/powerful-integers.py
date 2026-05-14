class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        
        res = set()
        
        a = 1
        while a <= bound:
            b = 1
            
            while a + b <= bound:
                res.add(a + b)
                
                if y == 1:
                    break
                b *= y
            
            if x == 1:
                break
            a *= x
        
        return list(res)