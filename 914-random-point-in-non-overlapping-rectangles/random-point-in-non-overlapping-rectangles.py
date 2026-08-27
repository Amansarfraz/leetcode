import random
import bisect

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.prefix_sums = []
        total_points = 0
        
        for x1, y1, x2, y2 in rects:
            # Number of integer points in the current rectangle
            # Elements are inclusive, so width is (x2 - x1 + 1) and height is (y2 - y1 + 1)
            points = (x2 - x1 + 1) * (y2 - y1 + 1)
            total_points += points
            self.prefix_sums.append(total_points)

    def pick(self):
        """
        :rtype: List[int]
        """
        # Pick a random point index out of the total pool of points
        target = random.randint(1, self.prefix_sums[-1])
        
        # Use binary search to find which rectangle contains this point index
        rect_idx = bisect.bisect_left(self.prefix_sums, target)
        
        # Get the chosen rectangle coordinates
        x1, y1, x2, y2 = self.rects[rect_idx]
        
        # Pick a random x and y coordinate inside this specific rectangle
        random_x = random.randint(x1, x2)
        random_y = random.randint(y1, y2)
        
        return [random_x, random_y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
