class Solution(object):
    def imageSmoother(self, img):
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                total = 0
                count = 0
                
                # check all 9 directions (including itself)
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if 0 <= r < rows and 0 <= c < cols:
                            total += img[r][c]
                            count += 1
                
                result[i][j] = total // count  # floor division
        
        return result