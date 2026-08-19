from collections import defaultdict

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # Map row -> bitmask of reserved seats
        occupied = defaultdict(int)
        for row, col in reservedSeats:
            occupied[row] |= (1 << col)
            
        # Start by assuming all rows can fit 2 families
        max_families = n * 2
        
        for row, mask in occupied.items():
            # Check the 3 possible 4-seat configurations
            # Left: columns 2, 3, 4, 5
            # Right: columns 6, 7, 8, 9
            # Middle: columns 4, 5, 6, 7
            
            left_free = not (mask & (1 << 2 | 1 << 3 | 1 << 4 | 1 << 5))
            right_free = not (mask & (1 << 6 | 1 << 7 | 1 << 8 | 1 << 9))
            middle_free = not (mask & (1 << 4 | 1 << 5 | 1 << 6 | 1 << 7))
            
            # Reduce count based on availability
            if left_free and right_free:
                continue # Row fits 2 families, no change needed
            elif left_free or right_free or middle_free:
                max_families -= 1 # Fits only 1 family instead of 2
            else:
                max_families -= 2 # Fits 0 families instead of 2
                
        return max_families
