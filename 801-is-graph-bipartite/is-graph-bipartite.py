class Solution(object):
    def isBipartite(self, graph):
        from collections import deque
        
        n = len(graph)
        color = {}
        
        for i in range(n):
            if i not in color:
                queue = deque([i])
                color[i] = 0
                
                while queue:
                    node = queue.popleft()
                    
                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = 1 - color[node]
                            queue.append(nei)
                        elif color[nei] == color[node]:
                            return False
        
        return True