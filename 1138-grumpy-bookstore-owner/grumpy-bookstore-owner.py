class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        
        n = len(customers)
        
        # Jo customers already satisfied hain
        satisfied = 0
        
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]

        # Sliding window for extra satisfied customers
        extra = 0
        
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra

        for i in range(minutes, n):
            # Window me naya add karo
            if grumpy[i] == 1:
                extra += customers[i]

            # Window se purana remove karo
            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]

            max_extra = max(max_extra, extra)

        return satisfied + max_extra