class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            
            if tx == ty:
                break
            
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    # ty == sy → check directly
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    # tx == sx → check directly
                    return (ty - sy) % tx == 0
        
        return tx == sx and ty == sy