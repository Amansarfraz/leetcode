class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        unique_types = len(set(candyType))
        
        return min(unique_types, n // 2)