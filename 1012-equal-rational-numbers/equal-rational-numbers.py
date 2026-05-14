from fractions import Fraction

class Solution(object):
    def isRationalEqual(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def convert(num):
            if '(' not in num:
                return Fraction(num)
            
            non_repeat, repeat = num.split('(')
            repeat = repeat[:-1]
            
            if '.' in non_repeat:
                integer, decimal = non_repeat.split('.')
            else:
                integer, decimal = non_repeat, ""
            
            integer = int(integer)
            
            # Non-repeating part
            result = Fraction(integer)
            
            if decimal:
                result += Fraction(int(decimal), 10 ** len(decimal))
            
            # Repeating part
            if repeat:
                repeating_value = int(repeat)
                repeating_len = len(repeat)
                non_repeat_len = len(decimal)
                
                result += Fraction(
                    repeating_value,
                    (10 ** non_repeat_len) * (10 ** repeating_len - 1)
                )
            
            return result
        
        return convert(s) == convert(t)