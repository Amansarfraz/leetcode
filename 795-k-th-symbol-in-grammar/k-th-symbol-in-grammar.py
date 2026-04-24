class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        
        # if k is even → flip parent
        if k % 2 == 0:
            return 1 - parent
        
        return parent