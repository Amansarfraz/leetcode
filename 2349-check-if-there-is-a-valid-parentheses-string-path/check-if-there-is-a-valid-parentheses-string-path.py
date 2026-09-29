class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # Early optimization checks
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        if (m + n - 1) % 2 != 0:
            return False
            
        memo = {}
        
        def dfs(r, c, balance):
            # If closed parentheses outweigh open ones, it's invalid
            if balance < 0:
                # If there aren't enough remaining steps to close open parentheses
                return False
            if balance > (m - 1 - r) + (n - 1 - c):
                return False
                
            # Reached the end destination
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            state = (r, c, balance)
            if state in memo:
                return memo[state]
                
            # Explore moving down and right
            res = False
            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_bal = balance + (1 if grid[nr][nc] == '(' else -1)
                    if dfs(nr, nc, next_bal):
                        res = True
                        break
                        
            memo[state] = res
            return res
            
        # Start at (0, 0) with a balance of 1 (since grid[0][0] must be '(')
        return dfs(0, 0, 1)
