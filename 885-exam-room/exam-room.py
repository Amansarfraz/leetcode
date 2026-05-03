import bisect

class ExamRoom(object):

    def __init__(self, n):
        self.n = n
        self.seats = []  # sorted list

    def seat(self):
        if not self.seats:
            self.seats.append(0)
            return 0
        
        # max distance
        dist = self.seats[0]
        pos = 0
        
        # check gaps
        for i in range(len(self.seats) - 1):
            a = self.seats[i]
            b = self.seats[i + 1]
            
            d = (b - a) // 2
            if d > dist:
                dist = d
                pos = a + d
        
        # check end
        if self.n - 1 - self.seats[-1] > dist:
            pos = self.n - 1
        
        bisect.insort(self.seats, pos)
        return pos

    def leave(self, p):
        self.seats.remove(p)