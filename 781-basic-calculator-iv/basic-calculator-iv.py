class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        from collections import Counter
        
        eval_map = dict(zip(evalvars, evalints))
        
        # Polynomial class
        class Poly(Counter):
            def __add__(self, other):
                res = Poly(self)
                for k, v in other.items():
                    res[k] += v
                return res
            
            def __sub__(self, other):
                res = Poly(self)
                for k, v in other.items():
                    res[k] -= v
                return res
            
            def __mul__(self, other):
                res = Poly()
                for k1, v1 in self.items():
                    for k2, v2 in other.items():
                        res[tuple(sorted(k1 + k2))] += v1 * v2
                return res
        
        def make(token):
            if token.isdigit():
                return Poly({(): int(token)})
            if token in eval_map:
                return Poly({(): eval_map[token]})
            return Poly({(token,): 1})
        
        # precedence function
        def precedence(op):
            if op == '*':
                return 2
            return 1
        
        def parse(expr):
            stack = []
            ops = []
            
            def apply():
                right = stack.pop()
                left = stack.pop()
                op = ops.pop()
                if op == '+':
                    stack.append(left + right)
                elif op == '-':
                    stack.append(left - right)
                else:
                    stack.append(left * right)
            
            i = 0
            while i < len(expr):
                if expr[i] == ' ':
                    i += 1
                    continue
                
                # parentheses
                if expr[i] == '(':
                    j = i
                    bal = 0
                    while i < len(expr):
                        if expr[i] == '(':
                            bal += 1
                        elif expr[i] == ')':
                            bal -= 1
                        if bal == 0:
                            break
                        i += 1
                    stack.append(parse(expr[j+1:i]))
                
                # variable or number
                elif expr[i].isalnum():
                    j = i
                    while i < len(expr) and expr[i].isalnum():
                        i += 1
                    stack.append(make(expr[j:i]))
                    i -= 1
                
                # operator
                elif expr[i] in '+-*':
                    while ops and precedence(ops[-1]) >= precedence(expr[i]):
                        apply()
                    ops.append(expr[i])
                
                i += 1
            
            while ops:
                apply()
            
            return stack[-1]
        
        poly = parse(expression)
        
        # format result
        result = []
        for key in sorted(poly.keys(), key=lambda x: (-len(x), x)):
            coeff = poly[key]
            if coeff == 0:
                continue
            term = str(coeff)
            for var in key:
                term += '*' + var
            result.append(term)
        
        return result