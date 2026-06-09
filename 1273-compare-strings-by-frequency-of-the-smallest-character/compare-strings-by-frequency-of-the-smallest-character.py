from bisect import bisect_right

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def f(s):
            smallest = min(s)
            return s.count(smallest)
        
        word_freqs = sorted(f(w) for w in words)
        n = len(word_freqs)
        
        ans = []
        for q in queries:
            fq = f(q)
            ans.append(n - bisect_right(word_freqs, fq))
        
        return ans