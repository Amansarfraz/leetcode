from collections import Counter

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        count = Counter(tiles)

        def backtrack():
            total = 0

            for ch in count:
                if count[ch] == 0:
                    continue

                total += 1
                count[ch] -= 1
                total += backtrack()
                count[ch] += 1

            return total

        return backtrack()