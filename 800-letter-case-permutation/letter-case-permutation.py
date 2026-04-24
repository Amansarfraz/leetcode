
class Solution(object):
    def letterCasePermutation(self, s):
        res = []
        
        def dfs(i, path):
            if i == len(s):
                res.append(path)
                return
            
            if s[i].isalpha():
                # lowercase choice
                dfs(i + 1, path + s[i].lower())
                # uppercase choice
                dfs(i + 1, path + s[i].upper())
            else:
                dfs(i + 1, path + s[i])
        
        dfs(0, "")
        return res