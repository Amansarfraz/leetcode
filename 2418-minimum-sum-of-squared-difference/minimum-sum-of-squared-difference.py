class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        n = len(nums1)
        k = k1 + k2
        
        # Calculate absolute differences
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        total_diff = sum(diffs)
        
        # If total operations are enough to zero out all differences
        if total_diff <= k:
            return 0
        
        # Initialize the frequency array correctly with [0]
        max_val = max(diffs)
        count = [0] * (max_val + 1)
        for d in diffs:
            count[d] += 1
            
        # Greedily reduce from the largest difference down
        for i in range(max_val, 0, -1):
            if count[i] > 0:
                take = min(k, count[i])
                count[i] -= take
                count[i - 1] += take
                k -= take
                if k == 0:
                    break
                    
        # Calculate the final sum of squared differences
        return sum(c * (i * i) for i, c in enumerate(count))
