class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        from collections import deque
        
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = set([startGene])
        genes = ['A', 'C', 'G', 'T']
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == endGene:
                return steps
            
            # try all mutations
            for i in range(len(curr)):
                for g in genes:
                    if curr[i] == g:
                        continue
                    
                    new_gene = curr[:i] + g + curr[i+1:]
                    
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))
        
        return -1