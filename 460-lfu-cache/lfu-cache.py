from collections import defaultdict, OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}  # key -> (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> keys in LRU order

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_val_freq:
            return -1
        
        value, freq = self.key_to_val_freq[key]
        # Remove from old freq list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        
        # Add to new freq list
        freq += 1
        self.freq_to_keys[freq][key] = None
        self.key_to_val_freq[key] = (value, freq)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return
        
        if key in self.key_to_val_freq:
            # Update value and increase freq
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self.get(key)  # update frequency
            return
        
        if len(self.key_to_val_freq) >= self.capacity:
            # Evict LFU key
            lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[lfu_key]
        
        # Insert new key with freq 1
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1