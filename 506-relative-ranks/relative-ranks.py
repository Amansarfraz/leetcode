class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        # Sort indices by score in descending order
        sorted_indices = sorted(range(n), key=lambda i: -score[i])
        
        result = [""] * n
        for rank, idx in enumerate(sorted_indices):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        
        return result