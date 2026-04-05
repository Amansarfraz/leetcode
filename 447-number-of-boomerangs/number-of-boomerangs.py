class Solution(object):
    def numberOfBoomerangs(self, points):
        res = 0
        
        for i in range(len(points)):
            dist_map = {}
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                
                dist = dx*dx + dy*dy  # squared distance
                
                dist_map[dist] = dist_map.get(dist, 0) + 1
            
            for count in dist_map.values():
                res += count * (count - 1)
        
        return res