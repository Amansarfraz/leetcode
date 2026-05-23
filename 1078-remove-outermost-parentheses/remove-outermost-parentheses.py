class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result = []
        balance = 0
        
        for ch in s:
            
            # Opening bracket
            if ch == '(':
                
                # Not outermost
                if balance > 0:
                    result.append(ch)
                
                balance += 1
            
            # Closing bracket
            else:
                
                balance -= 1
                
                # Not outermost
                if balance > 0:
                    result.append(ch)
        
        return ''.join(result)