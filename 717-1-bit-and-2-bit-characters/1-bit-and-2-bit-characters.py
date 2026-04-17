class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)
        
        # process until last character
        while i < n - 1:
            if bits[i] == 1:
                i += 2  # 2-bit character
            else:
                i += 1  # 1-bit character
        
        # if we end exactly at last index, it's valid 1-bit char
        return i == n - 1