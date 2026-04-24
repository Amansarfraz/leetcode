class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)   # for O(1) lookup
        count = 0
        
        for ch in stones:
            if ch in jewel_set:
                count += 1
                
        return count