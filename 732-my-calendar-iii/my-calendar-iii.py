class MyCalendarThree(object):

    def __init__(self):
        self.timeline = {}

    def book(self, startTime, endTime):
        # mark start
        self.timeline[startTime] = self.timeline.get(startTime, 0) + 1
        # mark end
        self.timeline[endTime] = self.timeline.get(endTime, 0) - 1

        # compute max overlap
        active = 0
        ans = 0

        for time in sorted(self.timeline):
            active += self.timeline[time]
            ans = max(ans, active)

        return ans


# Example:
# obj = MyCalendarThree()
# print(obj.book(10, 20))  # 1
# print(obj.book(50, 60))  # 1
# print(obj.book(10, 40))  # 2
# print(obj.book(5, 15))   # 3