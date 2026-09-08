class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If the number is less than 1000, no numbers in the range contain commas.
        if n < 1000:
            return 0
        
        total_commas = 0
        # Start looking from the first threshold where commas appear (1,000)
        start = 1000
        commas_per_number = 1
        
        while start <= n:
            # The current bracket goes up to 999, 999,999, etc.
            end = start * 1000 - 1
            
            # If n falls within this bracket, we only count up to n
            current_end = min(n, end)
            
            # Total numbers in this bracket
            count_of_numbers = current_end - start + 1
            
            # Add commas contributed by this bracket
            total_commas += count_of_numbers * commas_per_number
            
            # Move to the next bracket (e.g., 1,000,000)
            start *= 1000
            commas_per_number += 1
            
        return total_commas
