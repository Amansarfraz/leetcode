class Solution(object):
    def frequencySort(self, s):
        freq = {}
        
        # Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Sort by frequency (descending)
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Build result
        res = ""
        for ch, count in sorted_chars:
            res += ch * count
        
        return res