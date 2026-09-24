class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        # Create a list filled with None, sized n + 1 to handle 1-indexed idKeys
        self.stream = [None] * (n + 1)
        # The pointer starts at the first expected ID, which is 1
        self.ptr = 1

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        # Store the value at its respective 1-indexed position
        self.stream[idKey] = value
        
        result = []
        
        # If the newly inserted item matches the current pointer, 
        # collect all consecutive non-empty values
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1
            
        return result
