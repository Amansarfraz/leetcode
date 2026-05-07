class Solution(object):
    def orderlyQueue(self, s, k):
        if k == 1:
            # find smallest rotation
            res = s
            for i in range(len(s)):
                rotated = s[i:] + s[:i]
                if rotated < res:
                    res = rotated
            return res
        else:
            # can fully rearrange
            return ''.join(sorted(s))