class Solution(object):
    def carFleet(self, target, position, speed):
        # Pair position with time to reach target
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        for pos, spd in cars:
            time = float(target - pos) / spd
            
            # If this car forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: it joins the fleet ahead (do nothing)
        
        return len(stack)