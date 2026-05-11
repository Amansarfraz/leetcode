class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        from collections import deque
        
        deck.sort()
        n = len(deck)
        
        q = deque(range(n))
        res = [0] * n
        
        for card in deck:
            idx = q.popleft()
            res[idx] = card
            
            if q:
                q.append(q.popleft())
        
        return res