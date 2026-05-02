class Solution(object):
    def loudAndRich(self, richer, quiet):
        from collections import defaultdict
        
        # Build graph: poorer -> richer
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        
        n = len(quiet)
        answer = [-1] * n
        
        def dfs(node):
            # If already computed, return it
            if answer[node] != -1:
                return answer[node]
            
            # Initially, assume the quietest is the person itself
            answer[node] = node
            
            # Check all richer people
            for nei in graph[node]:
                candidate = dfs(nei)
                
                # Compare quietness
                if quiet[candidate] < quiet[answer[node]]:
                    answer[node] = candidate
            
            return answer[node]
        
        # Run DFS for each person
        for i in range(n):
            dfs(i)
        
        return answer