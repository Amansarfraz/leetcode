class Solution(object):
    def findComplement(self, num):
        # edge case: num = 0
        if num == 0:
            return 1
        
        # number of bits in num
        length = num.bit_length()
        
        # mask with all 1s for the bit length
        mask = (1 << length) - 1
        
        return num ^ mask