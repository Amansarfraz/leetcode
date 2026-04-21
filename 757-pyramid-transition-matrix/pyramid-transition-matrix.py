class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        from collections import defaultdict
        
        # Build mapping
        mp = defaultdict(list)
        for s in allowed:
            mp[s[:2]].append(s[2])
        
        # DFS to build pyramid
        def dfs(curr):
            if len(curr) == 1:
                return True
            
            # generate all possible next rows
            def build_next(i, path):
                if i == len(curr) - 1:
                    return dfs(path)
                
                pair = curr[i:i+2]
                if pair not in mp:
                    return False
                
                for ch in mp[pair]:
                    if build_next(i + 1, path + ch):
                        return True
                
                return False
            
            return build_next(0, "")
        
        return dfs(bottom)