class Solution(object):
    def customSortString(self, order, s):
        from collections import Counter
        
        count = Counter(s)
        result = []
        
        # Add characters in order
        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]
        
        # Add remaining characters
        for ch in count:
            result.append(ch * count[ch])
        
        return "".join(result)