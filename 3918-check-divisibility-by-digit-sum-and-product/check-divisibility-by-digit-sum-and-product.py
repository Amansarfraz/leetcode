class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Create variables to track the digit sum and product
        digit_sum = 0
        digit_product = 1
        
        # Keep a copy of the original number to extract digits
        temp = n
        
        while temp > 0:
            # Extract the last digit and reduce the number
            temp, digit = divmod(temp, 10)
            
            # Update the sum and product
            digit_sum += digit
            digit_product *= digit
            
        # Check if n is perfectly divisible by the total sum
        return n % (digit_sum + digit_product) == 0
