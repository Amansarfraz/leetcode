import random
from collections import defaultdict

class Solution(object):
    def findSecretWord(self, words, master):

        def match(a, b):
            return sum(x == y for x, y in zip(a, b))

        while words:
            # choose best guess
            count = {}
            for w1 in words:
                groups = [0] * 7
                for w2 in words:
                    if w1 != w2:
                        groups[match(w1, w2)] += 1
                count[w1] = max(groups)

            guess = min(words, key=lambda w: count[w])

            score = master.guess(guess)
            if score == 6:
                return

            # filter words
            words = [w for w in words if match(w, guess) == score]