class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        n = len(boxes)
        
        # dp[r + 1] stores the minimum trips needed to deliver boxes from 0 to r
        dp = [0] * (n + 1)
        
        trips = 2      # Starts with 2 trips: storage -> first port and last port -> storage
        weight = 0     # Track current shipment total weight
        l = 0          # Left boundary of our sliding window
        
        for r in range(n):
            weight += boxes[r][1]
            
            # If the current box's destination differs from the previous one, 
            # it requires an additional intermediate trip.
            if r > 0 and boxes[r][0] != boxes[r - 1][0]:
                trips += 1
                
            # Shrink the window from the left if constraints are violated:
            # 1. Total box count exceeds maxBoxes
            # 2. Total weight exceeds maxWeight
            # 3. Optimization: if dp[l + 1] == dp[l], it is always optimal to defer 
            #    the box 'l' to the next trip without penalizing total trip counts.
            while (r - l + 1 > maxBoxes or 
                   weight > maxWeight or 
                   (l < r and dp[l + 1] == dp[l])):
                weight -= boxes[l][1]
                if boxes[l][0] != boxes[l + 1][0]:
                    trips -= 1
                l += 1
                
            # Transition: Best result using boxes up to r is the cost of delivering
            # boxes up to l-1, plus the optimal trip segment cost calculated for the window [l...r]
            dp[r + 1] = dp[l] + trips
            
        return dp[n]
