class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        def isLeap(y):
            return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

        days = ["Friday", "Saturday", "Sunday", "Monday",
                "Tuesday", "Wednesday", "Thursday"]

        monthDays = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

        total = 0

        for y in range(1971, year):
            total += 366 if isLeap(y) else 365

        for m in range(1, month):
            total += monthDays[m - 1]
            if m == 2 and isLeap(year):
                total += 1

        total += day - 1

        return days[total % 7]