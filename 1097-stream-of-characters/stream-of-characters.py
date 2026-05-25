class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """

        self.root = TrieNode()
        self.stream = []
        self.maxLen = 0

        for word in words:
            self.maxLen = max(self.maxLen, len(word))

            node = self.root

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.isWord = True

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """

        self.stream.append(letter)

        if len(self.stream) > self.maxLen:
            self.stream.pop(0)

        node = self.root

        for ch in reversed(self.stream):

            if ch not in node.children:
                return False

            node = node.children[ch]

            if node.isWord:
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)