class Solution(object):
    def slidingPuzzle(self, board):
        from collections import deque
        
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        
        neighbors = {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4],
            4: [1,3,5],
            5: [2,4]
        }
        
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            state, steps = queue.popleft()
            
            if state == target:
                return steps
            
            zero_idx = state.index('0')
            
            for nei in neighbors[zero_idx]:
                new_state = list(state)
                new_state[zero_idx], new_state[nei] = new_state[nei], new_state[zero_idx]
                new_state = ''.join(new_state)
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
        
        return -1