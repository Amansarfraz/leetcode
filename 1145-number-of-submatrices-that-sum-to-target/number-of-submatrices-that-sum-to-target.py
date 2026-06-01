class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        
        # Row-wise prefix sums
        for r in range(m):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c - 1]
        
        result = 0
        
        # Fix left and right columns
        for left in range(n):
            for right in range(left, n):
                prefix = 0
                count = {0: 1}
                
                for r in range(m):
                    curr = matrix[r][right]
                    if left > 0:
                        curr -= matrix[r][left - 1]
                    
                    prefix += curr
                    result += count.get(prefix - target, 0)
                    count[prefix] = count.get(prefix, 0) + 1
        
        return result