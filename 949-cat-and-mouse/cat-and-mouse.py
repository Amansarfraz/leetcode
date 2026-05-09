from collections import deque

class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)

        # 0 = draw, 1 = mouse wins, 2 = cat wins
        color = [[[0] * 3 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 3 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(n):
                degree[m][c][1] = len(graph[m])
                degree[m][c][2] = len(graph[c])

                if 0 in graph[c]:
                    degree[m][c][2] -= 1

        queue = deque()

        for i in range(n):
            for turn in [1, 2]:
                color[0][i][turn] = 1
                queue.append((0, i, turn, 1))

                if i > 0:
                    color[i][i][turn] = 2
                    queue.append((i, i, turn, 2))

        while queue:
            m, c, turn, result = queue.popleft()

            for pm, pc, pturn in self.parents(graph, m, c, turn):
                if color[pm][pc][pturn] != 0:
                    continue

                if pturn == result:
                    color[pm][pc][pturn] = result
                    queue.append((pm, pc, pturn, result))
                else:
                    degree[pm][pc][pturn] -= 1
                    if degree[pm][pc][pturn] == 0:
                        color[pm][pc][pturn] = 3 - pturn
                        queue.append((pm, pc, pturn, 3 - pturn))

        return color[1][2][1]

    def parents(self, graph, m, c, turn):
        if turn == 1:
            for pc in graph[c]:
                if pc != 0:
                    yield m, pc, 2
        else:
            for pm in graph[m]:
                yield pm, c, 1