import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # Append original index to each interval: (l, r, weight, original_idx)
        # Sort primarily by start time 'l'
        sorted_intervals = sorted((interval[0], interval[1], interval[2], i) 
                                  for i, interval in enumerate(intervals))
        
        n = len(sorted_intervals)
        
        # Extract only the start times to make binary searching easier
        starts = [item[0] for item in sorted_intervals]
        
        # dp[i][j] holds a tuple: (max_weight, list_of_sorted_original_indices)
        # where i is the current interval index, and j is the number of chosen intervals (0 to 4)
        # Base cases initialization: all combinations start with weight 0 and empty choices
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        # Fill the DP table backwards from the last interval down to 0
        for i in range(n - 1, -1, -1):
            l, r, w, idx = sorted_intervals[i]
            
            # Find the next interval that does not overlap (next_start > current_end)
            # Since intervals sharing a boundary overlap, we look for start > r
            next_idx = bisect.bisect_right(starts, r)
            
            for j in range(1, 5):
                # Option 1: Skip the current interval
                skip_w, skip_indices = dp[i + 1][j]
                
                # Option 2: Take the current interval
                take_w, take_indices = dp[next_idx][j - 1]
                current_take_w = take_w + w
                
                # Create the newly formed index selection, maintaining ascending sorted order
                current_take_indices = sorted(take_indices + [idx])
                
                # Compare both strategies
                if current_take_w > skip_w:
                    dp[i][j] = (current_take_w, current_take_indices)
                elif skip_w > current_take_w:
                    dp[i][j] = (skip_w, skip_indices)
                else:
                    # If weights are identical, pick the lexicographically smaller index list
                    if current_take_indices < skip_indices:
                        dp[i][j] = (current_take_w, current_take_indices)
                    else:
                        dp[i][j] = (skip_w, skip_indices)
                        
        # The answer will be the highest scoring outcome across choosing 1, 2, 3, or 4 intervals
        best_w = -1
        best_indices = []
        
        for j in range(1, 5):
            w, indices = dp[0][j]
            if w > best_w:
                best_w = w
                best_indices = indices
            elif w == best_w:
                if indices < best_indices:
                    best_indices = indices
                    
        return best_indices
