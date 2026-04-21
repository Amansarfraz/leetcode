class Solution(object):
    def makeLargestSpecial(self, s):
        if len(s) <= 2:
            return s
        
        res = []
        count = 0
        start = 0
        
        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1
            
            # found a valid special substring
            if count == 0:
                # remove outer 1 and 0, recurse inside
                inner = self.makeLargestSpecial(s[start+1:i])
                res.append('1' + inner + '0')
                start = i + 1
        
        # sort in descending order
        res.sort(reverse=True)
        
        return ''.join(res)