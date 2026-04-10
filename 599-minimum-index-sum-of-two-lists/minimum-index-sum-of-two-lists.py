class Solution(object):
    def findRestaurant(self, list1, list2):
        index = {v: i for i, v in enumerate(list1)}
        
        best = float('inf')
        res = []

        for j, v in enumerate(list2):
            if v in index:
                s = j + index[v]
                if s < best:
                    best = s
                    res = [v]
                elif s == best:
                    res.append(v)

        return res