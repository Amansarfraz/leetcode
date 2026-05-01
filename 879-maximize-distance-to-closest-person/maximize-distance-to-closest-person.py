class Solution(object):
    def maxDistToClosest(self, seats):

        max_dist = 0
        last = -1   # last occupied seat index

        for i in range(len(seats)):

            if seats[i] == 1:

                if last == -1:
                    # starting zeros
                    max_dist = i
                else:
                    # middle zeros
                    max_dist = max(max_dist, (i - last) // 2)

                last = i

        # ending zeros
        max_dist = max(max_dist, len(seats) - 1 - last)

        return max_dist