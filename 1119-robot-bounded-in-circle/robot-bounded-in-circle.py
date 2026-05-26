class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        # North, East, South, West
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        x = y = 0
        d = 0  # facing north

        for ch in instructions:
            if ch == 'G':
                x += directions[d][0]
                y += directions[d][1]

            elif ch == 'L':
                d = (d - 1) % 4

            else:  # 'R'
                d = (d + 1) % 4

        # Robot is bounded if:
        # 1. returns to origin OR
        # 2. does not face north
        return (x == 0 and y == 0) or d != 0