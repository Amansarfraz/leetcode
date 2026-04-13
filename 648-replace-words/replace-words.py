class Solution(object):
    def replaceWords(self, dictionary, sentence):
        
        root_set = set(dictionary)
        words = sentence.split()

        def find_root(word):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in root_set:
                    return prefix
            return word

        return " ".join(find_root(word) for word in words)