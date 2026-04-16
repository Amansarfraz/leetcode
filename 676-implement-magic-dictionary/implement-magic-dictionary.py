class MagicDictionary(object):

    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        self.words = set(dictionary)

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        for i in range(len(searchWord)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == searchWord[i]:
                    continue

                candidate = searchWord[:i] + ch + searchWord[i+1:]
                if candidate in self.words:
                    return True

        return False