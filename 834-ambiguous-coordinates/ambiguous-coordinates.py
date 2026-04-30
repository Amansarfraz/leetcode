class Solution(object):
    def ambiguousCoordinates(self, s):
        s = s[1:-1]  # remove parentheses
        
        def generate(num):
            res = []
            n = len(num)
            
            # Case 1: no decimal
            if num == "0" or not (num[0] == '0' and n > 1):
                res.append(num)
            
            # Case 2: with decimal
            for i in range(1, n):
                left = num[:i]
                right = num[i:]
                
                # skip invalid
                if (left[0] == '0' and len(left) > 1):
                    continue
                if right[-1] == '0':
                    continue
                
                res.append(left + "." + right)
            
            return res
        
        result = []
        
        # try all splits
        for i in range(1, len(s)):
            left_part = s[:i]
            right_part = s[i:]
            
            left_options = generate(left_part)
            right_options = generate(right_part)
            
            for l in left_options:
                for r in right_options:
                    result.append("(" + l + ", " + r + ")")
        
        return result