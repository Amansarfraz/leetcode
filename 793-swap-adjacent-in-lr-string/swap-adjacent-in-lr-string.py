class Solution(object):
    def canTransform(self, start, result):
        # Condition 1: same sequence without X
        if start.replace('X','') != result.replace('X',''):
            return False
        
        i = j = 0
        n = len(start)
        
        while i < n and j < n:
            # skip X
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1
            
            if i == n and j == n:
                return True
            
            if i == n or j == n:
                return False
            
            # check movement rules
            if start[i] != result[j]:
                return False
            
            # L cannot move right
            if start[i] == 'L' and i < j:
                return False
            
            # R cannot move left
            if start[i] == 'R' and i > j:
                return False
            
            i += 1
            j += 1
        
        return True