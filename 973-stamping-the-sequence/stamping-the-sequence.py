class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        
        m, n = len(stamp), len(target)
        target = list(target)
        res = []
        visited = [False] * (n - m + 1)
        stars = 0
        
        def can_replace(pos):
            for i in range(m):
                if (target[pos + i] != '*' and
                    target[pos + i] != stamp[i]):
                    return False
            return True
        
        def do_replace(pos):
            count = 0
            
            for i in range(m):
                if target[pos + i] != '*':
                    target[pos + i] = '*'
                    count += 1
            
            return count
        
        while stars < n:
            done_replace = False
            
            for i in range(n - m + 1):
                if not visited[i] and can_replace(i):
                    visited[i] = True
                    gained = do_replace(i)
                    
                    if gained > 0:
                        done_replace = True
                        stars += gained
                        res.append(i)
                    
                    if stars == n:
                        break
            
            if not done_replace:
                return []
        
        return res[::-1]