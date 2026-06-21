class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Step 1: sort unique values
        sorted_unique = sorted(set(arr))
        
        # Step 2: assign ranks
        rank = {}
        for i, val in enumerate(sorted_unique):
            rank[val] = i + 1
        
        # Step 3: replace with rank
        return [rank[x] for x in arr]