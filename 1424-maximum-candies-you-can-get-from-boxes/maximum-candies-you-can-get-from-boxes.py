from collections import deque

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        n = len(status)

        have_box = [False] * n
        opened = [False] * n

        q = deque()

        for box in initialBoxes:
            have_box[box] = True
            if status[box] == 1:
                q.append(box)

        total = 0

        while q:
            box = q.popleft()

            if opened[box]:
                continue

            opened[box] = True
            total += candies[box]

            for key in keys[box]:
                status[key] = 1
                if have_box[key] and not opened[key]:
                    q.append(key)

            for new_box in containedBoxes[box]:
                have_box[new_box] = True
                if status[new_box] == 1 and not opened[new_box]:
                    q.append(new_box)

        return total