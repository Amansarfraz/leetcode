class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        operations = 0

        while target > startValue:
            operations += 1

            if target % 2 == 0:
                target //= 2
            else:
                target += 1

        return operations + (startValue - target)