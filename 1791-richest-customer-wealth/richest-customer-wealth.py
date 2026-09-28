class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Sum each inner list (customer accounts) and return the maximum value
        return max(sum(customer) for customer in accounts)
