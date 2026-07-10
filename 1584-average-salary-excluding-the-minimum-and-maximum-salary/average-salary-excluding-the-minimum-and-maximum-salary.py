class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return float(sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)