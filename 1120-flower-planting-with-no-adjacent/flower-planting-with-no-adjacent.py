class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        
        graph = [[] for _ in range(n)]

        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        flowers = [0] * n

        for i in range(n):
            used = set()

            for neighbor in graph[i]:
                if flowers[neighbor] != 0:
                    used.add(flowers[neighbor])

            for flower in range(1, 5):
                if flower not in used:
                    flowers[i] = flower
                    break

        return flowers