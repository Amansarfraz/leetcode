class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute Pascal's Triangle for combinations C(n, k)
        # This bypasses the need for math.comb() entirely
        C = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
        
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            # Use our precomputed combination table
            interleave_ways = C[len(left) + len(right)][len(left)]
            
            return (interleave_ways * dfs(left) * dfs(right)) % MOD
            
        return (dfs(nums) - 1) % MOD
