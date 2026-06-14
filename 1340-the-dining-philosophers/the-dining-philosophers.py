import threading

class DiningPhilosophers(object):

    def __init__(self):
        self.locks = [threading.Lock() for _ in range(5)]

    def wantsToEat(self, philosopher,
                   pickLeftFork, pickRightFork,
                   eat, putLeftFork, putRightFork):

        left = philosopher
        right = (philosopher + 1) % 5

        # enforce ordering to avoid deadlock
        first = min(left, right)
        second = max(left, right)

        self.locks[first].acquire()
        self.locks[second].acquire()

        try:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
        finally:
            self.locks[second].release()
            self.locks[first].release()