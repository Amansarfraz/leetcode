class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        prev_smaller = [-1] * n
        next_smaller = [n] * n

        stack = []

        # Previous Smaller
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        # Next Smaller
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0

        for i in range(n):
            left = i - prev_smaller[i]
            right = next_smaller[i] - i

            ans += arr[i] * left * right
            ans %= MOD

        return ans