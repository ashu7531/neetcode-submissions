class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.time = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            value, _ = self.cache[key]
            self.time += 1
            self.cache[key] = (value, self.time)
            return value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.time += 1
            self.cache[key] = (value, self.time)
        else:
            if len(self.cache) >= self.size:
                lru_key = min(self.cache, key=lambda k : self.cache[k][1])
                del self.cache[lru_key]
            self.time += 1
            self.cache[key] = (value, self.time)

