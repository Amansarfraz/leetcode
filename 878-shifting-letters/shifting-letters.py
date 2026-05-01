class Solution(object):
    def shiftingLetters(self, s, shifts):

        n = len(s)
        res = list(s)

        total = 0

        for i in range(n - 1, -1, -1):
            total = (total + shifts[i]) % 26

            # shift character
            new_char = (ord(res[i]) - ord('a') + total) % 26
            res[i] = chr(new_char + ord('a'))

        return "".join(res)