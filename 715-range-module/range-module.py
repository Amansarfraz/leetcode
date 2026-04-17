class RangeModule(object):

    def __init__(self):
        self.intervals = []

    def addRange(self, left, right):
        new = []
        i = 0
        n = len(self.intervals)

        # add all intervals before
        while i < n and self.intervals[i][1] < left:
            new.append(self.intervals[i])
            i += 1

        # merge overlapping
        while i < n and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1

        new.append([left, right])

        # add remaining
        while i < n:
            new.append(self.intervals[i])
            i += 1

        self.intervals = new

    def queryRange(self, left, right):
        for l, r in self.intervals:
            if l <= left and right <= r:
                return True
            if l > left:
                break
        return False

    def removeRange(self, left, right):
        new = []

        for l, r in self.intervals:
            # no overlap
            if r <= left or l >= right:
                new.append([l, r])
            else:
                # left part remains
                if l < left:
                    new.append([l, left])
                # right part remains
                if r > right:
                    new.append([right, r])

        self.intervals = new