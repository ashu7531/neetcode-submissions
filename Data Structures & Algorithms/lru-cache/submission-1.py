class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.store = {}  # To store {key: (value, timestamp)}
        self.time = 0  # To keep track of usage order

    def get(self, key: int) -> int:
        if key in self.store:
            value, _ = self.store[key]
            self.time += 1
            self.store[key] = (value, self.time)  # Update the timestamp
            return value
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            # Update existing key
            self.time += 1
            self.store[key] = (value, self.time)
        else:
            if len(self.store) >= self.size:
                # Evict the least recently used item
                lru_key = min(self.store, key=lambda k: self.store[k][1])
                del self.store[lru_key]
            self.time += 1
            self.store[key] = (value, self.time)
