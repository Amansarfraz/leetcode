class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def book(self, startTime, endTime):
        for s, e in self.calendar:
            # overlap check
            if startTime < e and endTime > s:
                return False
        
        self.calendar.append((startTime, endTime))
        return True