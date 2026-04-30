class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image)
        
        for row in image:
            i, j = 0, len(row) - 1
            
            while i <= j:
                # swap + invert in one step
                row[i], row[j] = row[j] ^ 1, row[i] ^ 1
                i += 1
                j -= 1
        
        return image