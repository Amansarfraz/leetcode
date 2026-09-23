class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        v, h = destination
        result = []
        
        # Helper function to compute combinations manually without math.comb
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n // 2:
                r = n - r
            num = 1
            den = 1
            for i in range(1, r + 1):
                num *= (n - r + i)
                den *= i
            return num // den

        while h > 0 and v > 0:
            # Calculate remaining combinations manually
            remaining_combinations = nCr(h - 1 + v, h - 1)
            
            if k <= remaining_combinations:
                result.append('H')
                h -= 1
            else:
                result.append('V')
                k -= remaining_combinations
                v -= 1
        
        # Append any remaining steps
        result.append('H' * h)
        result.append('V' * v)
                
        return "".join(result)
