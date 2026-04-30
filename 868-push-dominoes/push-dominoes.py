class Solution(object):
    def pushDominoes(self, dominoes):
        s = "L" + dominoes + "R"
        res = list(s)
        
        prev = 0
        
        for i in range(1, len(s)):
            if s[i] == '.':
                continue
            
            if s[prev] == s[i]:
                # same force → fill same direction
                for k in range(prev + 1, i):
                    res[k] = s[i]
            
            elif s[prev] == 'R' and s[i] == 'L':
                # opposite forces → meet in middle
                l, r = prev + 1, i - 1
                while l < r:
                    res[l] = 'R'
                    res[r] = 'L'
                    l += 1
                    r -= 1
            
            # move previous force pointer
            prev = i
        
        return "".join(res[1:-1])