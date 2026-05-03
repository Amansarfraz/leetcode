from collections import defaultdict, deque

class Solution(object):
    def distanceK(self, root, target, k):
        # Step 1: Build graph (adjacency list)
        graph = defaultdict(list)
        
        def build(node, parent):
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build(node.left, node)
            build(node.right, node)
        
        build(root, None)
        
        # Step 2: BFS from target
        q = deque([(target, 0)])
        visited = set([target])
        res = []
        
        while q:
            node, dist = q.popleft()
            
            if dist == k:
                res.append(node.val)
            
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, dist + 1))
        
        return res