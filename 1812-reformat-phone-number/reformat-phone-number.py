class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        # Step 1: Clean the string by removing spaces and dashes
        digits = number.replace(" ", "").replace("-", "")
        
        chunks = []
        i = 0
        n = len(digits)
        
        # Step 2: Group into blocks of 3 while more than 4 digits remain
        while n - i > 4:
            chunks.append(digits[i:i+3])
            i += 3
            
        # Step 3: Handle the remaining digits (2, 3, or 4 digits left)
        rem = n - i
        if rem == 4:
            # Split 4 digits into two blocks of 2
            chunks.append(digits[i:i+2])
            chunks.append(digits[i+2:i+4])
        else:
            # 2 or 3 digits left form a single block
            chunks.append(digits[i:])
            
        # Step 4: Join all blocks with dashes
        return "-".join(chunks)
