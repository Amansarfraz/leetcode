class Solution(object):
    def possibleBipartition(self, n, dislikes):
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        
        # build graph
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if color[i] != 0:
                continue
            
            queue = deque([i])
            color[i] = 1
            
            while queue:
                node = queue.popleft()
                
                for nei in graph[node]:
                    if color[nei] == 0:
                        color[nei] = -color[node]
                        queue.append(nei)
                    
                    elif color[nei] == color[node]:
                        return False
        
        return True