class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """

        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def check(x, y):
            left = 0
            right = len(x) - 1

            while left < right and x[left] == y[right]:
                left += 1
                right -= 1

            return (left >= right or
                    is_palindrome(x, left, right) or
                    is_palindrome(y, left, right))

        return check(a, b) or check(b, a)

