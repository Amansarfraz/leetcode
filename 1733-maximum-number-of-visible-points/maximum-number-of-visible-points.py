import math

class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        my_x, my_y = location
        angles = []
        always_visible = 0
        
        # Step 1: Calculate polar angles in degrees relative to our location
        for px, py in points:
            if px == my_x and py == my_y:
                always_visible += 1
            else:
                # math.atan2 outputs radians; we convert it directly to degrees
                deg = math.degrees(math.atan2(py - my_y, px - my_x))
                angles.append(deg)
                
        # Step 2: Sort the calculated angles
        angles.sort()
        
        # Step 3: Duplicate the angles array with a +360 degree offset to handle circular wrap
        n = len(angles)
        for i in range(n):
            angles.append(angles[i] + 360.0)
            
        max_visible_in_window = 0
        left = 0
        
        # Step 4: Sliding window to find the densest angle interval
        for right in range(len(angles)):
            # If the current window bounds exceed our view span, contract from the left
            while angles[right] - angles[left] > angle:
                left += 1
                
            # Track the maximum count of valid coordinates observed in a single view frame
            max_visible_in_window = max(max_visible_in_window, right - left + 1)
            
        return max_visible_in_window + always_visible
