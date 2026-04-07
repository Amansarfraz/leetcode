class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0:
            return True
        
        total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if total_sum < desiredTotal:
            return False
        
        memo = {}
        
        def canWin(used, total):
            if used in memo:
                return memo[used]
            
            for i in range(1, maxChoosableInteger + 1):
                mask = 1 << i
                
                if used & mask == 0:  # number i not used
                    # if picking i wins OR opponent loses
                    if total + i >= desiredTotal or not canWin(used | mask, total + i):
                        memo[used] = True
                        return True
            
            memo[used] = False
            return False
        
        return canWin(0, 0)