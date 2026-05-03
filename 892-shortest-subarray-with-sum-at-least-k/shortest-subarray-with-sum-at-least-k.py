from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        n = len(nums)
        
        # Prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        dq = deque()
        res = float('inf')
        
        for i in range(n + 1):
            # Check if current prefix - smallest prefix >= k
            while dq and prefix[i] - prefix[dq[0]] >= k:
                res = min(res, i - dq.popleft())
            
            # Maintain increasing order of prefix sums
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return res if res != float('inf') else -1