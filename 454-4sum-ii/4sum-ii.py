class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count_map = {}
        
        # Step 1: store sums of nums1 + nums2
        for a in nums1:
            for b in nums2:
                s = a + b
                count_map[s] = count_map.get(s, 0) + 1
        
        res = 0
        
        # Step 2: check nums3 + nums4
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in count_map:
                    res += count_map[target]
        
        return res