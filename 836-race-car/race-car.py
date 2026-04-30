from collections import deque

class Solution(object):
    def racecar(self, target):
        queue = deque([(0, 1, 0)])  # (position, speed, steps)
        visited = set([(0, 1)])
        
        while queue:
            pos, speed, steps = queue.popleft()
            
            if pos == target:
                return steps
            
            # Accelerate
            new_pos = pos + speed
            new_speed = speed * 2
            
            if (new_pos, new_speed) not in visited and 0 <= new_pos <= 2 * target:
                visited.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, steps + 1))
            
            # Reverse
            rev_speed = -1 if speed > 0 else 1
            if (pos, rev_speed) not in visited:
                visited.add((pos, rev_speed))
                queue.append((pos, rev_speed, steps + 1))
        
        return -1