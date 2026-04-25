class Solution(object):
    def rotatedDigits(self, n):
        def isGood(num):
            changed = False
            
            while num > 0:
                d = num % 10
                
                if d in [3, 4, 7]:
                    return False
                
                if d in [2, 5, 6, 9]:
                    changed = True
                
                num //= 10
            
            return changed
        
        count = 0
        for i in range(1, n + 1):
            if isGood(i):
                count += 1
        
        return count