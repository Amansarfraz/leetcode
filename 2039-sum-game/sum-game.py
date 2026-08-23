class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0
        
        # Count sums and question marks for both halves
        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    left_q += 1
                else:
                    left_sum += int(num[i])
            else:
                if num[i] == '?':
                    right_q += 1
                else:
                    right_sum += int(num[i])
        
        # Alice wins if the total number of question marks is odd
        if (left_q + right_q) % 2 == 1:
            return True
            
        # Balance the equation: (Left Sum - Right Sum) == 9 * (Right Questions - Left Questions) / 2
        return (left_sum - right_sum) != 9 * (right_q - left_q) // 2
