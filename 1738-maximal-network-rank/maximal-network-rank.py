class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        degree = [0] * n
        connected = set()
        
        # Calculate degree of every city
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected.add((a, b))
            connected.add((b, a))
        
        max_rank = 0
        
        # Check every pair of cities
        for i in range(n):
            for j in range(i + 1, n):
                
                rank = degree[i] + degree[j]
                
                # If i and j are directly connected,
                # count that road only once
                if (i, j) in connected:
                    rank -= 1
                
                max_rank = max(max_rank, rank)
        
        return max_rank

