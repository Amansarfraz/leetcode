class Solution(object):
    def findMinMoves(self, machines):
        total = sum(machines)
        n = len(machines)
        
        # If not divisible, impossible
        if total % n != 0:
            return -1
        
        target = total // n
        max_moves = 0
        prefix_sum = 0
        
        for m in machines:
            diff = m - target
            prefix_sum += diff
            
            max_moves = max(max_moves, abs(prefix_sum), diff)
        
        return max_moves