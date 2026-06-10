from threading import Semaphore

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.cur = 1

        self.fizz_sem = Semaphore(0)
        self.buzz_sem = Semaphore(0)
        self.fizzbuzz_sem = Semaphore(0)
        self.number_sem = Semaphore(1)

    def _next(self):
        self.cur += 1

        if self.cur > self.n:
            self.fizz_sem.release()
            self.buzz_sem.release()
            self.fizzbuzz_sem.release()
            self.number_sem.release()
        elif self.cur % 15 == 0:
            self.fizzbuzz_sem.release()
        elif self.cur % 3 == 0:
            self.fizz_sem.release()
        elif self.cur % 5 == 0:
            self.buzz_sem.release()
        else:
            self.number_sem.release()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        while True:
            self.fizz_sem.acquire()
            if self.cur > self.n:
                return
            printFizz()
            self._next()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        while True:
            self.buzz_sem.acquire()
            if self.cur > self.n:
                return
            printBuzz()
            self._next()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        while True:
            self.fizzbuzz_sem.acquire()
            if self.cur > self.n:
                return
            printFizzBuzz()
            self._next()

    # printNumber(x) outputs "x"
    def number(self, printNumber):
        while True:
            self.number_sem.acquire()
            if self.cur > self.n:
                return

            if self.cur % 3 != 0 and self.cur % 5 != 0:
                printNumber(self.cur)

            self._next()