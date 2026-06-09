import heapq

class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        while self.available and (
            self.available[0] >= len(self.stacks) or
            len(self.stacks[self.available[0]]) == self.capacity
        ):
            heapq.heappop(self.available)

        if not self.available:
            self.stacks.append([])
            idx = len(self.stacks) - 1
        else:
            idx = heapq.heappop(self.available)

        self.stacks[idx].append(val)

        if len(self.stacks[idx]) < self.capacity:
            heapq.heappush(self.available, idx)

    def pop(self):
        """
        :rtype: int
        """
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        if not self.stacks:
            return -1

        idx = len(self.stacks) - 1
        val = self.stacks[idx].pop()

        heapq.heappush(self.available, idx)

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return val

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()
        heapq.heappush(self.available, index)

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return val