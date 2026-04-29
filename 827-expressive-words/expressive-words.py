class Solution(object):
    def expressiveWords(self, s, words):
        
        def get_groups(string):
            groups = []
            i = 0
            n = len(string)
            
            while i < n:
                j = i
                while j < n and string[j] == string[i]:
                    j += 1
                groups.append((string[i], j - i))
                i = j
            
            return groups
        
        s_groups = get_groups(s)
        count = 0
        
        for word in words:
            w_groups = get_groups(word)
            
            if len(s_groups) != len(w_groups):
                continue
            
            valid = True
            
            for (c1, n1), (c2, n2) in zip(s_groups, w_groups):
                if c1 != c2:
                    valid = False
                    break
                
                if n1 < 3 and n1 != n2:
                    valid = False
                    break
                
                if n1 >= 3 and n2 > n1:
                    valid = False
                    break
            
            if valid:
                count += 1
        
        return count