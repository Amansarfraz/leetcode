class Solution(object):
    def judgeSquareSum(self, c):
        import math
        
        a = 0
        b = int(math.sqrt(c))
        
        while a <= b:
            s = a*a + b*b
            
            if s == c:
                return True
            elif s < c:
                a += 1
            else:
                b -= 1
        
        return False