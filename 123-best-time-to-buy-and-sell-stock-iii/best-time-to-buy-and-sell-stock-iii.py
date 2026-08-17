
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
            
        # Cost variables track net expense (lower is better)
        # Profit variables track net returns (higher is better)
        buy1, buy2 = float('inf'), float('inf')
        profit1, profit2 = 0, 0
        
        for price in prices:
            # First transaction updates
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            
            # Second transaction updates (reinvesting profit from the first)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
            
        return profit2
