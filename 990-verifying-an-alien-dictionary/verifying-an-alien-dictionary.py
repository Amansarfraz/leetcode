class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        rank = {c: i for i, c in enumerate(order)}
        
        def compare(w1, w2):
            n1, n2 = len(w1), len(w2)
            for i in range(min(n1, n2)):
                if w1[i] != w2[i]:
                    return rank[w1[i]] - rank[w2[i]]
            return n1 - n2
        
        for i in range(len(words) - 1):
            if compare(words[i], words[i + 1]) > 0:
                return False
        
        return True