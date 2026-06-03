from threading import Semaphore

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.zero_sem = Semaphore(1)
        self.odd_sem = Semaphore(0)
        self.even_sem = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in xrange(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber(0)

            if i % 2:
                self.odd_sem.release()
            else:
                self.even_sem.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in xrange(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in xrange(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.zero_sem.release()