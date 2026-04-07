class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 3:
            return 1  # "1", "12", "122" all have 1 '1'
        
        s = [1, 2, 2]
        head = 2  # pointer for reading how many times to append
        tail = 3  # pointer for next position to append
        while len(s) < n:
            next_num = 3 - s[-1]  # toggle between 1 and 2
            for _ in range(s[head]):
                s.append(next_num)
            head += 1
        
        return s[:n].count(1)