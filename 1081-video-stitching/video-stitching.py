class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        
        # Sort by starting time
        clips.sort()
        
        count = 0
        current_end = 0
        farthest = 0
        i = 0
        n = len(clips)
        
        # Greedy coverage
        while current_end < time:
            
            # Extend coverage using all clips
            # starting before or at current_end
            while i < n and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1
            
            # Cannot extend further
            if farthest == current_end:
                return -1
            
            # Use one more clip
            count += 1
            current_end = farthest
        
        return count