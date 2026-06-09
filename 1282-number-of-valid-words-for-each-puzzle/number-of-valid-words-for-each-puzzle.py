from collections import Counter

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        freq = Counter()

        for word in words:
            mask = 0
            for ch in set(word):
                mask |= 1 << (ord(ch) - ord('a'))

            if bin(mask).count('1') <= 7:
                freq[mask] += 1

        ans = []

        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))

            mask = 0
            for ch in puzzle:
                mask |= 1 << (ord(ch) - ord('a'))

            sub = mask
            count = 0

            while sub:
                if sub & first:
                    count += freq[sub]
                sub = (sub - 1) & mask

            ans.append(count)

        return ans