class Solution(object):
    def solveEquation(self, equation):
        
        def parse(expr):
            x_coeff = 0
            const = 0
            i = 0
            sign = 1
            
            while i < len(expr):
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                else:
                    num = 0
                    is_num = False
                    
                    while i < len(expr) and expr[i].isdigit():
                        num = num * 10 + int(expr[i])
                        i += 1
                        is_num = True
                    
                    if i < len(expr) and expr[i] == 'x':
                        if is_num:
                            x_coeff += sign * num
                        else:
                            x_coeff += sign * 1
                        i += 1
                    else:
                        const += sign * num
            
            return x_coeff, const
        
        left, right = equation.split('=')
        
        lx, lc = parse(left)
        rx, rc = parse(right)
        
        # Move everything to left side
        x = lx - rx
        c = rc - lc
        
        if x == 0:
            if c == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        return "x=" + str(c // x)