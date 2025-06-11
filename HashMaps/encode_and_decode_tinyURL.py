class Codec:
    """
    Hash Map 
    
    Intuition: 
        This approach uses a dictionary to maintain a one-to-one mapping between
        the original long URLs and their shortened versions.

    Time Complexity: O(1)
    Space Complexity: O(n)
    """

    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl):
        shortUrl = "http://tinyurl.com/" + str(self.counter)
        self.url_map[shortUrl] = longUrl
        self.counter += 1
        return shortUrl

    def decode(self, shortUrl):
        return self.url_map.get(shortUrl, "")
