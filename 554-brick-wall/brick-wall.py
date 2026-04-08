class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        edge_count = defaultdict(int)
        
        for row in wall:
            pos = 0
            # Skip last brick to avoid counting rightmost edge
            for brick in row[:-1]:
                pos += brick
                edge_count[pos] += 1
        
        if not edge_count:
            return len(wall)
        
        # Maximum edges aligned -> minimum bricks crossed
        max_edges = max(edge_count.values())
        return len(wall) - max_edges