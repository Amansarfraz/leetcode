class Solution(object):
    def maxProfit(self, prices, fee):
        hold = -prices[0]   # buying first stock
        cash = 0            # no stock
        
        for price in prices[1:]:
            # update states
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)
        
        return cash