from collections import Counter

class Solution(object):
    def findLUSlength(self, strs):
        count = Counter(strs)
        # Sort by length descending
        strs.sort(key=len, reverse=True)
        
        for i, s in enumerate(strs):
            if count[s] > 1:
                continue  # skip duplicates
            if all(not self.isSubsequence(s, t) for j, t in enumerate(strs) if s != t):
                return len(s)
        
        return -1
    
    def isSubsequence(self, s, t):
        it = iter(t)
        return all(c in it for c in s)