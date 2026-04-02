class Solution(object):
    def reconstructQueue(self, people):
        # Step 1: Sort by height descending, k ascending
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Step 2: Insert each person at index k
        queue = []
        for p in people:
            queue.insert(p[1], p)
        
        return queue