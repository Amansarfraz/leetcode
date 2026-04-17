from collections import defaultdict

class Solution(object):
    def countOfAtoms(self, formula):
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                
                # read multiplier
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                
                mult = int(formula[start:i] or 1)
                
                for atom, count in top.items():
                    stack[-1][atom] += count * mult
            
            else:
                # parse element name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                
                atom = formula[start:i]
                
                # parse number
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                
                count = int(formula[start:i] or 1)
                
                stack[-1][atom] += count
        
        # final result
        result = stack[0]
        
        return "".join(
            atom + (str(result[atom]) if result[atom] > 1 else "")
            for atom in sorted(result)
        )