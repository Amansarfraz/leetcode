from threading import Semaphore

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foo_sem = Semaphore(1)
        self.bar_sem = Semaphore(0)

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.foo_sem.acquire()

            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()

            self.bar_sem.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.bar_sem.acquire()

            # printBar() outputs "bar". Do not change or remove this line.
            printBar()

            self.foo_sem.release()