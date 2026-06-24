class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        def isLeap(year):
            return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

        def daysFrom1971(date):
            year, month, day = map(int, date.split('-'))

            days = 0

            for y in range(1971, year):
                days += 366 if isLeap(y) else 365

            monthDays = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

            for m in range(1, month):
                days += monthDays[m - 1]
                if m == 2 and isLeap(year):
                    days += 1

            days += day

            return days

        return abs(daysFrom1971(date1) - daysFrom1971(date2))