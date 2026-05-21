class Solution(object):
    def gridIllumination(self, n, lamps, queries):
        """
        :type n: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        rows = {}
        cols = {}
        diag = {}
        anti = {}
        
        active = set()
        
        for r, c in lamps:
            if (r, c) in active:
                continue
                
            active.add((r, c))
            
            rows[r] = rows.get(r, 0) + 1
            cols[c] = cols.get(c, 0) + 1
            diag[r - c] = diag.get(r - c, 0) + 1
            anti[r + c] = anti.get(r + c, 0) + 1
        
        ans = []
        
        directions = [
            (0, 0), (0, 1), (0, -1),
            (1, 0), (-1, 0),
            (1, 1), (1, -1),
            (-1, 1), (-1, -1)
        ]
        
        for r, c in queries:
            
            if (rows.get(r, 0) > 0 or
                cols.get(c, 0) > 0 or
                diag.get(r - c, 0) > 0 or
                anti.get(r + c, 0) > 0):
                ans.append(1)
            else:
                ans.append(0)
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if (nr, nc) in active:
                    active.remove((nr, nc))
                    
                    rows[nr] -= 1
                    cols[nc] -= 1
                    diag[nr - nc] -= 1
                    anti[nr + nc] -= 1
        
        return ans