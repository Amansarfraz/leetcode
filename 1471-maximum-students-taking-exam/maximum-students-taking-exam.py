class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        m, n = len(seats), len(seats[0])

        valid_masks = []

        for r in range(m):
            masks = []
            for mask in range(1 << n):
                ok = True

                # broken seats
                for c in range(n):
                    if (mask & (1 << c)) and seats[r][c] == '#':
                        ok = False
                        break

                # adjacent students in same row
                if mask & (mask << 1):
                    ok = False

                if ok:
                    masks.append(mask)

            valid_masks.append(masks)

        dp = {0: 0}

        for r in range(m):
            ndp = {}

            for mask in valid_masks[r]:
                students = bin(mask).count('1')

                for prev_mask, prev_val in dp.items():

                    # upper-left and upper-right cheating
                    if (mask & (prev_mask << 1)) or (mask & (prev_mask >> 1)):
                        continue

                    ndp[mask] = max(
                        ndp.get(mask, 0),
                        prev_val + students
                    )

            dp = ndp

        return max(dp.values()) if dp else 0