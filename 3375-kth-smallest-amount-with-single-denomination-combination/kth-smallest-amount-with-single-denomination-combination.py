import math
import fractions  # <-- Import the fractions module for Python 2

class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        n = len(coins)
        lcm_cache = []
        
        for i in range(1, 1 << n):
            current_lcm = 1
            bits_count = 0
            for j in range(n):
                if (i >> j) & 1:
                    bits_count += 1
                    # Use fractions.gcd instead of math.gcd
                    current_lcm = (current_lcm * coins[j]) // fractions.gcd(current_lcm, coins[j])
            lcm_cache.append((current_lcm, bits_count))
            
        def count_multiples(target):
            total = 0
            for lcm, size in lcm_cache:
                if size % 2 == 1:
                    total += target // lcm
                else:
                    total -= target // lcm
            return total

        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1  
            else:
                low = mid + 1   
                
        return ans
