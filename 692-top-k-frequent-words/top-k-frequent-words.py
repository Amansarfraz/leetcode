class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter

        count = Counter(words)

        sorted_words = sorted(count.keys(), key=lambda w: (-count[w], w))

        return sorted_words[:k]