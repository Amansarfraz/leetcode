class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        from collections import Counter

        available = Counter(letters)

        word_counts = []
        word_scores = []

        for word in words:
            cnt = Counter(word)
            word_counts.append(cnt)

            s = 0
            for ch in word:
                s += score[ord(ch) - ord('a')]
            word_scores.append(s)

        n = len(words)

        def dfs(i, remain):
            if i == n:
                return 0

            # Skip current word
            ans = dfs(i + 1, remain)

            # Take current word if possible
            cnt = word_counts[i]
            can_take = True

            for ch, freq in cnt.items():
                if remain[ch] < freq:
                    can_take = False
                    break

            if can_take:
                for ch, freq in cnt.items():
                    remain[ch] -= freq

                ans = max(ans, word_scores[i] + dfs(i + 1, remain))

                for ch, freq in cnt.items():
                    remain[ch] += freq

            return ans

        return dfs(0, available)