class Solution(object):
    def eventualSafeNodes(self, graph):
        from collections import deque
        
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        outdegree = [0] * n
        
        # Build reverse graph and outdegree
        for u in range(n):
            outdegree[u] = len(graph[u])
            for v in graph[u]:
                reverse_graph[v].append(u)
        
        # Start with terminal nodes
        queue = deque()
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)
        
        safe = [False] * n
        
        while queue:
            node = queue.popleft()
            safe[node] = True
            
            for prev in reverse_graph[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    queue.append(prev)
        
        # Collect safe nodes
        return [i for i in range(n) if safe[i]]