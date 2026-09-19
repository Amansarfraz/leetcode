class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # Find the x-coordinate of the nearest point on the rectangle to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        
        # Find the y-coordinate of the nearest point on the rectangle to the circle's center
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate the squared distance between the circle's center and this closest point
        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y
        squared_distance = (distance_x ** 2) + (distance_y ** 2)
        
        # If the squared distance is less than or equal to the squared radius, they overlap
        return squared_distance <= (radius ** 2)
