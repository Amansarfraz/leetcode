class Solution(object):
    def minSwap(self, nums1, nums2):
        n = len(nums1)
        
        keep = 0      # no swap at i
        swap = 1      # swap at i
        
        for i in range(1, n):
            new_keep = float('inf')
            new_swap = float('inf')
            
            # Case 1: no swap needed
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                new_keep = min(new_keep, keep)
                new_swap = min(new_swap, swap + 1)
            
            # Case 2: cross swap
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                new_keep = min(new_keep, swap)
                new_swap = min(new_swap, keep + 1)
            
            keep, swap = new_keep, new_swap
        
        return min(keep, swap)