class Solution(object):
    def longestWord(self, words):
        words.sort()
        words.sort(key=len)
        
        valid = set([""])
        ans = ""
        
        for w in words:
            if w[:-1] in valid:
                valid.add(w)
                
                if len(w) > len(ans) or (len(w) == len(ans) and w < ans):
                    ans = w
        
        return ans