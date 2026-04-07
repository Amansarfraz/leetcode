class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        
        import bisect
        res = 0
        
        for house in houses:
            # find the insertion position in heaters
            idx = bisect.bisect_left(heaters, house)
            
            left_dist = float('inf') if idx == 0 else house - heaters[idx - 1]
            right_dist = float('inf') if idx == len(heaters) else heaters[idx] - house
            
            res = max(res, min(left_dist, right_dist))
        
        return res