from collections import defaultdict, deque

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0

        # value -> all indices
        mp = defaultdict(list)
        for i, v in enumerate(arr):
            mp[v].append(i)

        q = deque([0])
        visited = set([0])
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # jump to same value indices
                for j in mp[arr[i]]:
                    if j not in visited:
                        visited.add(j)
                        q.append(j)

                # important optimization (avoid re-processing)
                mp[arr[i]] = []

                # left move
                if i - 1 >= 0 and i - 1 not in visited:
                    visited.add(i - 1)
                    q.append(i - 1)

                # right move
                if i + 1 < n and i + 1 not in visited:
                    visited.add(i + 1)
                    q.append(i + 1)

            steps += 1

        return -1