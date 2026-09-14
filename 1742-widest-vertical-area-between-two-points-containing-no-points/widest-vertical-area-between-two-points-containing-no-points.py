class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Extract and sort all x-coordinates
        x_coords = sorted([p[0] for p in points])
        
        # Find the maximum gap between consecutive x-coordinates
        max_width = 0
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i - 1])
            
        return max_width
