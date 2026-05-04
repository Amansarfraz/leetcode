class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        size = 0

        # Step 1: find total length
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        # Step 2: work backwards
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            k %= size

            if k == 0 and ch.isalpha():
                return ch

            if ch.isdigit():
                size //= int(ch)
            else:
                size -= 1