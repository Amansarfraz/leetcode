from collections import defaultdict

class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        sub_size = n // k
        
        # Early exit check via pigeonhole principle
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] > k:
                return -1
                
        # Precompute all valid standalone subsets of size `sub_size`
        valid_subsets = {}
        for mask in range(1 << n):
            if bin(mask).count('1') == sub_size:
                subset_vals = [nums[i] for i in range(n) if (mask & (1 << i))]
                if len(set(subset_vals)) == sub_size:
                    valid_subsets[mask] = max(subset_vals) - min(subset_vals)
                    
        # Correctly initialize the fixed-size array to infinity
        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0
        
        # Iterate sequentially through all possible mask states
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
                
            # Symmetry breaking: Find the first available unassigned element
            first_available = 0
            while first_available < n and (mask & (1 << first_available)):
                first_available += 1
                
            if first_available == n:
                continue
                
            # Transition to next states
            for sub_mask, cost in valid_subsets.items():
                # Enforce that the selected sub_mask must cover our first available element
                if not (sub_mask & (1 << first_available)):
                    continue
                # Ensure no overlapping elements are picked
                if (mask & sub_mask) == 0:
                    next_mask = mask | sub_mask
                    if dp[mask] + cost < dp[next_mask]:
                        dp[next_mask] = dp[mask] + cost
                        
        ans = dp[(1 << n) - 1]
        return ans if ans != INF else -1
