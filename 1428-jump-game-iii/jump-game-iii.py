from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        q = deque([start])
        visited = set([start])

        while q:
            i = q.popleft()

            if arr[i] == 0:
                return True

            for nei in (i + arr[i], i - arr[i]):
                if 0 <= nei < n and nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return False