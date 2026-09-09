class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_commas = 0
        factor = 1000
        commas_per_num = 1
        
        while n >= factor:
            # Determine the upper bound of the current comma tier
            next_factor = factor * 1000
            
            # Count how many numbers fall into the current tier
            count = min(n, next_factor - 1) - factor + 1
            
            # Add the commas contributed by this tier
            total_commas += count * commas_per_num
            
            # Move to the next tier (e.g., millions, billions)
            factor = next_factor
            commas_per_num += 1
            
        return total_commas
