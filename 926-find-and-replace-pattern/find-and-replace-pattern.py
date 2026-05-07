class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word, pattern):
            map_w_p = {}
            map_p_w = {}
            
            for w, p in zip(word, pattern):
                if w not in map_w_p and p not in map_p_w:
                    map_w_p[w] = p
                    map_p_w[p] = w
                else:
                    if map_w_p.get(w) != p or map_p_w.get(p) != w:
                        return False
            return True
        
        result = []
        for word in words:
            if match(word, pattern):
                result.append(word)
        
        return result