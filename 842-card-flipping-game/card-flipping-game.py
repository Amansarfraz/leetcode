class Solution(object):
    def flipgame(self, fronts, backs):
        bad = set()
        
        # Step 1: find invalid numbers
        for f, b in zip(fronts, backs):
            if f == b:
                bad.add(f)
        
        ans = float('inf')
        
        # Step 2: check all numbers
        for x in fronts + backs:
            if x not in bad:
                ans = min(ans, x)
        
        return ans if ans != float('inf') else 0