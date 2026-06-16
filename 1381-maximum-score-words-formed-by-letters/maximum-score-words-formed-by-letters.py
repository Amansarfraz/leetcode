class Solution(object):
    def maxScoreWords(self, words, letters, score):
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

            # option 1: skip word
            best = dfs(i + 1, remain)

            cnt = word_counts[i]

            # check if we can take word
            can_take = True
            for ch, freq in cnt.items():
                if remain[ch] < freq:
                    can_take = False
                    break

            if can_take:
                # choose
                for ch, freq in cnt.items():
                    remain[ch] -= freq

                best = max(best, word_scores[i] + dfs(i + 1, remain))

                # backtrack
                for ch, freq in cnt.items():
                    remain[ch] += freq

            return best

        return dfs(0, available)