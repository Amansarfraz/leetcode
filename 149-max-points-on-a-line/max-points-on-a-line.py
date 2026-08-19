from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n
            
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        max_points = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 1  # Tracks overlapping points at the exact same coordinates
            current_max = 0
            
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                # Handle identical points
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue
                    
                # Calculate rise and run
                dy = y2 - y1
                dx = x2 - x1
                
                # Reduce fraction using GCD to avoid floating-point inaccuracies
                gcd = get_gcd(dy, dx)
                slope_key = (dy // gcd, dx // gcd)
                
                slopes[slope_key] += 1
                current_max = max(current_max, slopes[slope_key])
                
            max_points = max(max_points, current_max + duplicate)
            
        return max_points
