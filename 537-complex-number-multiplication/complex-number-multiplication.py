class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        # Parse a+bi
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))
        
        real = a*c - b*d
        imag = a*d + b*c
        
        return "{}+{}i".format(real, imag)