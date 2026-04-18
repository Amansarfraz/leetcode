class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for a in asteroids:

            # collision only when stack top is moving right
            # and current asteroid is moving left
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()   # stack asteroid destroyed
                    continue
                elif stack[-1] == -a:
                    stack.pop()   # both destroyed
                break
            else:
                stack.append(a)

        return stack