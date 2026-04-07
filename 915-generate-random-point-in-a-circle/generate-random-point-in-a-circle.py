import random
import math

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        # random angle
        theta = random.uniform(0, 2 * math.pi)
        # random radius with sqrt scaling
        r = self.radius * math.sqrt(random.uniform(0, 1))
        
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        
        return [x, y]