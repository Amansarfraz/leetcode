class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        n = len(s)
        
        # store all operations by index
        ops = [[] for _ in range(n)]
        
        for i in range(len(indices)):
            idx = indices[i]
            ops[idx].append((sources[i], targets[i]))
        
        res = []
        i = 0
        
        while i < n:
            replaced = False
            
            # check all operations at this index
            for src, tgt in ops[i]:
                if s[i:i+len(src)] == src:
                    res.append(tgt)
                    i += len(src)
                    replaced = True
                    break
            
            if not replaced:
                res.append(s[i])
                i += 1
        
        return "".join(res)