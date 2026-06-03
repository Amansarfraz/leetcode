from threading import Lock

class Foo(object):
    def __init__(self):
        self.first_done = Lock()
        self.second_done = Lock()

        self.first_done.acquire()
        self.second_done.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.first_done.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        with self.first_done:
            printSecond()
            self.second_done.release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        with self.second_done:
            printThird()