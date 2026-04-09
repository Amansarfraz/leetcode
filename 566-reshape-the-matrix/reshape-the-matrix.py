class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        # check if reshape possible
        if m * n != r * c:
            return mat

        # flatten matrix
        flat = []
        for row in mat:
            for val in row:
                flat.append(val)

        # build new matrix
        res = []
        index = 0

        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(flat[index])
                index += 1
            res.append(new_row)

        return res