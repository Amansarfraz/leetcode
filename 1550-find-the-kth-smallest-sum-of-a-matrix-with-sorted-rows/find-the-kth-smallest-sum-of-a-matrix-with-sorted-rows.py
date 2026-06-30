import heapq

class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        sums = mat[0]

        for row in mat[1:]:
            heap = []
            visited = set()

            heapq.heappush(heap, (sums[0] + row[0], 0, 0))
            visited.add((0, 0))

            newSums = []

            while heap and len(newSums) < k:
                total, i, j = heapq.heappop(heap)
                newSums.append(total)

                if i + 1 < len(sums) and (i + 1, j) not in visited:
                    heapq.heappush(heap, (sums[i + 1] + row[j], i + 1, j))
                    visited.add((i + 1, j))

                if j + 1 < len(row) and (i, j + 1) not in visited:
                    heapq.heappush(heap, (sums[i] + row[j + 1], i, j + 1))
                    visited.add((i, j + 1))

            sums = newSums

        return sums[k - 1]