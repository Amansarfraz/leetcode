class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        total = sum(stones)
        target = total // 2
        
        dp = set([0])

        for stone in stones:
            new_dp = dp.copy()

            for s in dp:
                if s + stone <= target:
                    new_dp.add(s + stone)

            dp = new_dp

        best = max(dp)

        return total - 2 * best