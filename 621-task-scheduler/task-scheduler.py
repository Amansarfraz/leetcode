from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        
        max_freq = max(freq.values())
        
        max_count = 0
        for v in freq.values():
            if v == max_freq:
                max_count += 1
        
        part1 = (max_freq - 1) * (n + 1)
        part2 = max_count
        
        return max(len(tasks), part1 + part2)