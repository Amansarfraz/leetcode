class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        i = 0  # child index
        j = 0  # cookie index
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1  # child content
            j += 1  # move to next cookie
        
        return i