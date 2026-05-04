class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:

            # if light + heavy can go together
            if people[left] + people[right] <= limit:
                left += 1

            # always take the heavy person
            right -= 1
            boats += 1

        return boats