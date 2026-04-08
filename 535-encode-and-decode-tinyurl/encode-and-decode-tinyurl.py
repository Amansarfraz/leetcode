import random
import string

class Codec:

    def __init__(self):
        self.url_map = {}
        self.chars = string.ascii_letters + string.digits
        self.base_url = "http://tinyurl.com/"
    
    def generate_key(self, length=6):
        return ''.join(random.choice(self.chars) for _ in range(length))

    def encode(self, longUrl):
        key = self.generate_key()
        # Ensure key is unique
        while key in self.url_map:
            key = self.generate_key()
        self.url_map[key] = longUrl
        return self.base_url + key

    def decode(self, shortUrl):
        key = shortUrl.replace(self.base_url, "")
        return self.url_map.get(key, "")