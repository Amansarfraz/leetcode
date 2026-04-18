class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = image[sr][sc]
        
        # if no change needed
        if original == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # boundary + color check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original:
                return

            # fill color
            image[r][c] = color

            # explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image