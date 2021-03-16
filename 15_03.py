# Monday, 15th March 2021
# Encode and Decode TinyURL

class Codec:
    def __init__(self):
        self.lookup = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        n = len(self.lookup)
        self.lookup.append(longUrl)
        return "http://tinyurl.com/" + str(n)
    
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s = int(shortUrl.split('/')[-1])
        return self.lookup[s]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))