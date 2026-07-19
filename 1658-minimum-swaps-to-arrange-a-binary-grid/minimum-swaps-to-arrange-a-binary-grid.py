class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        # Count trailing zeros in each row
        zeros = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)

        swaps = 0

        for i in range(n):
            need = n - 1 - i

            # Find a row with enough trailing zeros
            j = i
            while j < n and zeros[j] < need:
                j += 1

            if j == n:
                return -1

            # Bring row j to position i using adjacent swaps
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                swaps += 1
                j -= 1

        return swaps