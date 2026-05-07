class RLEIterator(object):

    def __init__(self, encoding):
        self.encoding = encoding
        self.i = 0  # pointer to count

    def next(self, n):
        while self.i < len(self.encoding):
            count = self.encoding[self.i]
            value = self.encoding[self.i + 1]
            
            if count >= n:
                self.encoding[self.i] -= n
                return value
            else:
                n -= count
                self.i += 2  # move to next pair
        
        return -1