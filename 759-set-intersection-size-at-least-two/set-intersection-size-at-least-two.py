class Solution(object):
    def intersectionSizeTwo(self, intervals):
        # sort by end asc, start desc
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        a = -1   # second last chosen
        b = -1   # last chosen
        res = 0
        
        for start, end in intervals:
            if start > b:
                # need 2 new points
                res += 2
                a = end - 1
                b = end
            elif start > a:
                # need 1 new point
                res += 1
                a = b
                b = end
        
        return res