class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"

        # Handle negative numbers (32-bit)
        num &= 0xffffffff

        result = ""

        while num > 0:
            result = hex_chars[num % 16] + result
            num //= 16

        return result