class Fancy(object):

    def __init__(self):
        self.MOD = 10**9 + 7
        self.nums = []
        self.scale = 1   # Global multiplier tracking cumulative multAll calls
        self.bias = 0    # Global adder tracking cumulative addAll calls

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Reverse the current global scale and bias transformations before saving.
        # Formula: stored_val = (val - bias) / scale  (mod MOD)
        # Using pow(self.scale, self.MOD - 2, self.MOD) yields the modular inverse of scale.
        inv_scale = pow(self.scale, self.MOD - 2, self.MOD)
        stored_val = ((val - self.bias) * inv_scale) % self.MOD
        self.nums.append(stored_val)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        # Increment the global adder state
        self.bias = (self.bias + inc) % self.MOD

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        # Scale both the global multiplier and the existing adder state
        self.scale = (self.scale * m) % self.MOD
        self.bias = (self.bias * m) % self.MOD

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        # If the index is out of bounds, return -1 as required by the problem statement
        if idx >= len(self.nums):
            return -1
        
        # Apply the current global transformations to the stored core value
        # Formula: current_val = (stored_val * scale) + bias (mod MOD)
        return (self.nums[idx] * self.scale + self.bias) % self.MOD
