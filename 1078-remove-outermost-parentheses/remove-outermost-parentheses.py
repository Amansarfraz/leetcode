class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        opened = 0
        
        for char in s:
            if char == '(':
                # If opened > 0, this '(' is not the outermost one
                if opened > 0:
                    res.append(char)
                opened += 1
            else:
                opened -= 1
                # If opened > 0 after decrementing, this ')' is not the outermost one
                if opened > 0:
                    res.append(char)
                    
        return "".join(res)
