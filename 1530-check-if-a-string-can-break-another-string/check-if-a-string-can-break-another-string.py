class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = sorted(s1)
        s2 = sorted(s2)

        can1 = True
        can2 = True

        for i in range(len(s1)):
            if s1[i] < s2[i]:
                can1 = False
            if s2[i] < s1[i]:
                can2 = False

        return can1 or can2