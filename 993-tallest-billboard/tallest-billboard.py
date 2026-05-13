class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp = {0: 0}

        for rod in rods:
            cur = dp.copy()

            for diff, height in cur.items():
                
                dp[diff + rod] = max(dp.get(diff + rod, 0), height)

                
                new_diff = abs(diff - rod)
                new_height = height + min(diff, rod)

                dp[new_diff] = max(dp.get(new_diff, 0), new_height)

        return dp[0]