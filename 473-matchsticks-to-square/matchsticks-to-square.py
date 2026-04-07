class Solution(object):
    def makesquare(self, matchsticks):
        if not matchsticks:
            return False
        
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total // 4
        matchsticks.sort(reverse=True)
        
        sides = [0] * 4
        
        def dfs(index):
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == target
            
            for i in range(4):
                if sides[i] + matchsticks[index] > target:
                    continue
                
                sides[i] += matchsticks[index]
                
                if dfs(index + 1):
                    return True
                
                sides[i] -= matchsticks[index]
                
                # pruning: avoid duplicate states
                if sides[i] == 0:
                    break
            
            return False
        
        return dfs(0)