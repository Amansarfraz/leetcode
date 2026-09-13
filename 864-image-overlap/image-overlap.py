import collections

class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        # Get coordinates of all 1s in both images
        list1 = [(r, c) for r, row in enumerate(img1) for c, val in enumerate(row) if val == 1]
        list2 = [(r, c) for r, row in enumerate(img2) for c, val in enumerate(row) if val == 1]
        
        # Count the frequency of each translation vector (delta_r, delta_c)
        translation_counts = collections.Counter()
        
        for r1, c1 in list1:
            for r2, c2 in list2:
                # Calculate the shift required to move (r1, c1) to (r2, c2)
                vector = (r2 - r1, c2 - c1)
                translation_counts[vector] += 1
                
        # The maximum frequency is the largest overlap. 
        # If no 1s overlap, return 0.
        return max(translation_counts.values()) if translation_counts else 0
