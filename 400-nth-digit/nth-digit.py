class Solution(object):
    def findNthDigit(self, n):
        digit_length = 1   # digits per number (1,2,3...)
        count = 9          # how many numbers in this group
        start = 1          # starting number of this group

        # Step 1: Find the correct group
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        # Step 2: Find the actual number
        number = start + (n - 1) // digit_length

        # Step 3: Find the digit inside the number
        return int(str(number)[(n - 1) % digit_length])