class WordFilter(object):

    def __init__(self, words):
        self.lookup = {}
        
        for index, word in enumerate(words):
            length = len(word)
            
            for i in range(length + 1):
                pref = word[:i]
                for j in range(length + 1):
                    suff = word[j:]
                    
                    key = pref + "#" + suff
                    self.lookup[key] = index   # store latest index

    def f(self, pref, suff):
        return self.lookup.get(pref + "#" + suff, -1)