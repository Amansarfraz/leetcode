class Solution(object):
    def numSpecialEquivGroups(self, words):
        seen = set()
        
        for word in words:
            even = ''.join(sorted(word[0::2]))
            odd = ''.join(sorted(word[1::2]))
            
            seen.add((even, odd))
        
        return len(seen)