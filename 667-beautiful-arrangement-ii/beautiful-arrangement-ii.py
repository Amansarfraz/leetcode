class Solution(object):
    def constructArray(self, n, k):
        res = []
        
        left, right = 1, k + 1
        
        # create zig-zag to get k distinct differences
        while left <= right:
            if left == right:
                res.append(left)
            else:
                res.append(left)
                res.append(right)
            left += 1
            right -= 1
        
        # add remaining numbers
        for num in range(k + 2, n + 1):
            res.append(num)
        
        return res