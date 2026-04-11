class Solution(object):
    def maxDistance(self, arrays):
        
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        result = 0

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            # check distance using previous arrays
            result = max(result, abs(current_max - min_val))
            result = max(result, abs(max_val - current_min))

            # update global min/max
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return result