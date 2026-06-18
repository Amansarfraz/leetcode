class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.combinations = []
        self.index = 0

        def backtrack(start, path):
            if len(path) == combinationLength:
                self.combinations.append("".join(path))
                return

            for i in range(start, len(characters)):
                path.append(characters[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])

    def next(self):
        """
        :rtype: str
        """
        res = self.combinations[self.index]
        self.index += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()