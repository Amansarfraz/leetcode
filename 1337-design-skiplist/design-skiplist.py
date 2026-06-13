import random

class Node(object):
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level


class Skiplist(object):

    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.head = Node(-1, self.MAX_LEVEL)

    def _random_level(self):
        level = 1
        while level < self.MAX_LEVEL and random.random() < self.P:
            level += 1
        return level

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        curr = self.head

        for i in range(self.MAX_LEVEL - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]

        curr = curr.next[0]
        return curr is not None and curr.val == target

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        update = [None] * self.MAX_LEVEL
        curr = self.head

        for i in range(self.MAX_LEVEL - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr

        level = self._random_level()
        node = Node(num, level)

        for i in range(level):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        update = [None] * self.MAX_LEVEL
        curr = self.head

        for i in range(self.MAX_LEVEL - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr

        target = curr.next[0]

        if target is None or target.val != num:
            return False

        for i in range(len(target.next)):
            if update[i].next[i] == target:
                update[i].next[i] = target.next[i]

        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)