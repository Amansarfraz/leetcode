class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        # Initialize with the first key press details
        max_duration = releaseTimes[0]
        slowest_key = keysPressed[0]
        
        # Iterate through the rest of the key presses
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            key = keysPressed[i]
            
            # Update if we find a strictly longer duration,
            # or a tie with a lexicographically larger key
            if duration > max_duration:
                max_duration = duration
                slowest_key = key
            elif duration == max_duration and key > slowest_key:
                slowest_key = key
                
        return slowest_key
