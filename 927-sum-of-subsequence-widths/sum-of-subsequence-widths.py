class Solution(object):
    def sumSubseqWidths(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        
        nums.sort()
        
        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        result = 0
        
        for i in range(n):
            max_contribution = pow2[i]
            min_contribution = pow2[n - i - 1]
            
            result = (result + nums[i] * (max_contribution - min_contribution)) % MOD
        
        return result