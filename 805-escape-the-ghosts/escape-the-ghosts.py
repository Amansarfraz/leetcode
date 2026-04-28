class Solution(object):
    def escapeGhosts(self, ghosts, target):
        # Player distance from (0,0) to target
        d_player = abs(target[0]) + abs(target[1])
        
        for gx, gy in ghosts:
            d_ghost = abs(gx - target[0]) + abs(gy - target[1])
            
            if d_ghost <= d_player:
                return False
        
        return True