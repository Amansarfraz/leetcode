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
        closestX = min(max(xCenter, x1), x2)
        closestY = min(max(yCenter, y1), y2)

        dx = xCenter - closestX
        dy = yCenter - closestY

        return dx * dx + dy * dy <= radius * radius