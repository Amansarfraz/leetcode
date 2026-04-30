class Solution(object):
    def uniqueLetterString(self, s):
        n = len(s)
        
        index = {}
        
        # store positions of each character
        for i, ch in enumerate(s):
            index.setdefault(ch, []).append(i)
        
        res = 0
        
        for ch in index:
            arr = index[ch]
            
            # add boundaries
            arr = [-1] + arr + [n]
            
            for i in range(1, len(arr) - 1):
                left = arr[i] - arr[i - 1]
                right = arr[i + 1] - arr[i]
                res += left * right
        
        return res