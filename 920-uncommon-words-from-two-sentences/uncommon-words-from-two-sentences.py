class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        words = (s1 + " " + s2).split()
        
        freq = {}
        
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        
        result = []
        for w in freq:
            if freq[w] == 1:
                result.append(w)
        
        return result