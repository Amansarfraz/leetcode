class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        
        blocked = set(map(tuple, blocked))
        LIMIT = len(blocked) * (len(blocked) - 1) // 2

        def bfs(start, end):
            visited = set()
            queue = [tuple(start)]
            visited.add(tuple(start))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue and len(visited) <= LIMIT:
                x, y = queue.pop(0)

                if [x, y] == end:
                    return True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < 10**6 and
                        0 <= ny < 10**6 and
                        (nx, ny) not in blocked and
                        (nx, ny) not in visited):

                        visited.add((nx, ny))
                        queue.append((nx, ny))

            return len(visited) > LIMIT

        return bfs(source, target) and bfs(target, source)