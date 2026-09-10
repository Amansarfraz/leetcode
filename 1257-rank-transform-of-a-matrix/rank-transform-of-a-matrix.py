class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        # rank_row[r] tracks the largest rank used in row r so far
        # rank_col[c] tracks the largest rank used in column c so far
        rank_row = [0] * rows
        rank_col = [0] * cols
        
        # Group coordinate positions (r, c) by their matrix values
        from collections import defaultdict
        value_to_cells = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                value_to_cells[matrix[r][c]].append((r, c))
                
        # Result matrix to return
        answer = [[0] * cols for _ in range(rows)]
        
        # Process unique cell values in ascending order
        for val in sorted(value_to_cells.keys()):
            cells = value_to_cells[val]
            
            # --- DSU Implementation for the current group of identical values ---
            parent = {}
            def find(i):
                if parent[i] != i:
                    parent[i] = find(parent[i])
                return parent[i]
                
            def union(i, j):
                root_i = find(i)
                root_j = find(j)
                if root_i != root_j:
                    parent[root_i] = root_j

            # Initialize DSU parents for rows and columns occupied by these cells.
            # To avoid collision between row indices and col indices, offset col index by `rows`.
            for r, c in cells:
                if r not in parent: parent[r] = r
                if (c + rows) not in parent: parent[c + rows] = c + rows
                union(r, c + rows)
                
            # Group cells by their connected component root identifier
            components = defaultdict(list)
            for r, c in cells:
                root = find(r)
                components[root].append((r, c))
                
            # --- Calculate rank for each independent group ---
            for root, grouped_cells in components.items():
                # The minimum valid rank for this connected component must be 1 step greater 
                # than the maximum rank seen so far across all involved rows and columns.
                max_rank = 0
                for r, c in grouped_cells:
                    max_rank = max(max_rank, rank_row[r], rank_col[c])
                
                next_rank = max_rank + 1
                
                # Assign the calculated rank to the answer and update global tracking arrays
                for r, c in grouped_cells:
                    answer[r][c] = next_rank
                    rank_row[r] = next_rank
                    rank_col[c] = next_rank
                    
        return answer
