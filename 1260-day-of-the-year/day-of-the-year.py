class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = map(int, date.split('-'))

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        if leap:
            days[1] = 29

        return sum(days[:month - 1]) + day