class MyHashSet(object):

    def __init__(self):
        self.data = [False] * (10**6 + 1)

    def add(self, key):
        self.data[key] = True

    def remove(self, key):
        self.data[key] = False

    def contains(self, key):
        return self.data[key]