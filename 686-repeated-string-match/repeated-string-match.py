class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        repeated = a
        count = 1

        # repeat until length exceeds b
        while len(repeated) < len(b):
            repeated += a
            count += 1

        # check once
        if b in repeated:
            return count

        # check one more repeat (for overlap case)
        repeated += a
        if b in repeated:
            return count + 1

        return -1